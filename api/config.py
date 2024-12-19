import os

ERROR_CODE = int(os.getenv("ERROR_CODE", "500"))
ERROR_MESSAGE = os.getenv("ERROR_MESSAGE", "I am just a code-500 returner")