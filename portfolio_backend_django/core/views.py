
import logging

import redis


from django.conf import settings
from django.http import JsonResponse
from django.views import View

from pymongo import MongoClient

from core.util import *



myapp_logger = logging.getLogger("myapp")
msg_prettifier = MessagePrettifier("django")






# mongo client makes a connection pool having already open connections but specified as 0 for performance, 
# redis client does not have already open ones.
# mongo client opens a connection when the pool does not have any available one, redis client too.

mongo_client = MongoClient(settings.MONGODB_HOST, maxPoolSize=10000) 		
personality_db = mongo_client["personality"]
character_a_personality_collection = personality_db["character_a"]

redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)



# Django does not provide a built-in view class returning an json, but only templates,
# it is the only way to make a view returning an json that inherits the basic view class.

class VideoPersonalityFetchViewWithRedisConnectionpool(View):
	def get(self, request, video_personality_doc_id):
		video_personality_doc_cache = redis_client.hgetall(video_personality_doc_id)

		if video_personality_doc_cache != {}:
			prettifed_cache = msg_prettifier.prettify_json(video_personality_doc_cache)
			myapp_logger.info(f'a cache hit:\n{prettifed_cache}') 
			return JsonResponse(video_personality_doc_cache, json_dumps_params={"ensure_ascii": False})

		video_personality_doc = character_a_personality_collection.find_one({"_id": video_personality_doc_id})
		prettifed_doc = msg_prettifier.prettify_json(video_personality_doc)
		myapp_logger.info(f'fetched from mongodb:\n{prettifed_doc}') 


		# writing the fetched document/record to redis,
		# implementing an optimistic lock in case of concurrent writings.
		
		with redis_client.pipeline() as p:
			try:
				p.watch(video_personality_doc["_id"])

				p.multi()
				p.hset(video_personality_doc["_id"], mapping=video_personality_doc)
				p.expire(video_personality_doc["_id"], time=60)     
				p.execute()

				myapp_logger.info(f'a cache set:\n{prettifed_doc}')
				p.unwatch()
				return JsonResponse(video_personality_doc, json_dumps_params={"ensure_ascii": False})

			except Exception as e:
				myapp_logger.exception(f'error:\n{e}')
				p.unwatch()
				return JsonResponse(video_personality_doc, json_dumps_params={"ensure_ascii": False})
	


class VideoPersonalityFetchViewWithDefaultMongoDB(View):
	def get(self, request, video_personality_doc_id):
		# as this client is different from the global client, this client does not belong to the connection pool.
		# this client is created for each user request, makes each connection per each request.
		mongo_client = MongoClient(settings.MONGODB_HOST, connectTimeoutMS=None) 		
		personality_db = mongo_client["personality"]
		character_a_personality_collection = personality_db["character_a"]

		video_personality_doc = character_a_personality_collection.find_one({"_id": video_personality_doc_id})
		prettifed_doc = msg_prettifier.prettify_json(video_personality_doc)
		myapp_logger.info(f'fetched from mongodb:\n{prettifed_doc}') 

		return JsonResponse(video_personality_doc, json_dumps_params={"ensure_ascii": False})



class VideoPersonalityFetchViewWithMongoDBConnectionpool(View):
	def get(self, request, video_personality_doc_id):
		# this view uses the global mongodb client, which has a connection pool.
		video_personality_doc = character_a_personality_collection.find_one({"_id": video_personality_doc_id})
		prettifed_doc = msg_prettifier.prettify_json(video_personality_doc)
		myapp_logger.info(f'fetched from mongodb:\n{prettifed_doc}') 

		return JsonResponse(video_personality_doc, json_dumps_params={"ensure_ascii": False})