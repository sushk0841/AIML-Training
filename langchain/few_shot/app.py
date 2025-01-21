from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

examples=[{
    "word": "up",
    "opposite": "down"
},
{
    "word": "left",
    "opposite": "right"
},
{
    "word": "north",
    "opposite": "south"
},
{
    "word": "round",
    "opposite": "square"
}]


example_prompt=PromptTemplate(
    input_variables=["word", "opposite"],
    template=" word : {word}\n Opposite: {opposite}"
)

from langchain_core.prompts import FewShotPromptTemplate

prompt=FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="oppsoite word for {input} is ",
    input_variables=["input"]
    
    )

ollama_base_url=os.getenv("OLLAMA_BASE_URL")

llm=OllamaLLM(model="llama3.2",temperature=0.25,base_url=ollama_base_url)

chain=prompt | llm

results=chain.invoke({"input":"more"})
print(results)