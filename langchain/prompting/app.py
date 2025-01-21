# PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()


ollama_base_url=os.getenv("OLLAMA_BASE_URL")

llm=ChatOllama(model="llama3.2",temperature=0.25,base_url=ollama_base_url)
# if you use ChatOllama then you will get metadata too in the response .
prompt_template = PromptTemplate.from_template("Tell me a Joke {topic}")

chain = prompt_template | llm

results=chain.invoke({"topic:moon"})

print(results)


# chatpromptTEmpate

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

llm=OllamaLLM(model="llama3.2",temperature=0.25,base_url=ollama_base_url)

chat_prompt_template= ChatPromptTemplate(
    [
        ("system", "You are a helpful teacher"),
        ("user", "Tell me a joke about {topic}")
    ]
)

chain= chat_prompt_template | llm

results=chain.invoke({"topic":"moon"})

print(results)