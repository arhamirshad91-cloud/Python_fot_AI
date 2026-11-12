import os
from dotenv import load_dotenv

load_dotenv

LLMs = {
    "grok" : {
        "baseurl" : "http://api.groq.com/openai/v1"
        "apikey" : os.getenv("OPEN_ROUTER_KEY")
        "model" : "openai/gpt-oss-120b"
    },

}