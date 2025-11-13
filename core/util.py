
import logging
import traceback
import json



# NOTE:
# a try-except statement is implemented,
# unless an letting error-causing statement occur an error is effective.

myapp_logger = logging.getLogger("myapp")



class MessagePrettifier:
	def __init__(self, mode):
		self.mode = mode

    # different from the original json specification,
    # this is about json python deals with.
	def prettify_json(self, data):
		try:
			data = json.dumps(data, indent=4, ensure_ascii=False)
			return str(data)

		except Exception as e:
			if self.mode == 'django':
				myapp_logger.exception(f'an error occured. returning the msg as it is.\n{e}')
			elif self.mode == 'util':
				print(f'an error occured. returning the msg as it is.\n{traceback.format_exc()}')

			return str(data)