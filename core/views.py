
import logging

import redis


from django.conf import settings
from django.http import JsonResponse
from django.views import View

from pymongo import MongoClient

from core.util import *



# Django does not provide a built-in view class returning an json, but only templates,
# it is the only way to make a view returning an json that inherits the basic view class.



myapp_logger = logging.getLogger("myapp")

msg_prettifier = MessagePrettifier("django")



class VideoPersonalityFetchView(View):
	def get(self, request, video_personality_doc_id):
		mongo_client = MongoClient(settings.MONGODB_HOST) 		
		personality_db = mongo_client["personality"]
		character_a_personality_collection = personality_db["character_a"]

		redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)


		video_personality_doc_cache = redis_client.hgetall(video_personality_doc_id)

		if video_personality_doc_cache != {}:
			prettifed_cache = msg_prettifier.prettify_json(video_personality_doc_cache)
			myapp_logger.info(f'a cache hit:\n{prettifed_cache}') 
			return JsonResponse(video_personality_doc_cache, json_dumps_params={"ensure_ascii": False})


		video_personality_doc = character_a_personality_collection.find_one({"_id": video_personality_doc_id})
		prettifed_doc = msg_prettifier.prettify_json(video_personality_doc)
		myapp_logger.info(f'fetched from mongodb:\n{prettifed_doc}') 


		# writing the fetched document/record to redis,
		# implementing an optimistic lock in case of multiple writings.

		with redis_client.pipeline() as p:
			try:
				p.watch(video_personality_doc["_id"])

				p.multi()
				p.hset(video_personality_doc["_id"], mapping=video_personality_doc)
				p.expire(video_personality_doc["_id"], time=60)     
				p.execute()
				
				myapp_logger.info(f'a cache set:\n{prettifed_doc}')

			except Exception as e:
				myapp_logger.exception(f'error:\n{e}')

			finally:
				p.unwatch()     


		return JsonResponse(video_personality_doc, json_dumps_params={"ensure_ascii": False})
	

