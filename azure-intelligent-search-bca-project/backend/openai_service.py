import openai
from config import OPENAI_ENDPOINT, OPENAI_KEY

openai.api_type = "azure"
openai.api_base = OPENAI_ENDPOINT
openai.api_key = OPENAI_KEY