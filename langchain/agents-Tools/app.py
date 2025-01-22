# from dotenv import load_dotenv
# from langchain import hub
# from langchain.agents import (
#     AgentExecutor,
#     create_react_agent,
# )
# from langchain_core.tools import Tool
# from langchain_ollama import OllamaLLM

# # Load environment variables from .env file
# load_dotenv()


# # Define a very simple tool function that returns the current time
# def get_current_time(*args, **kwargs):
#     """Returns the current time in H:MM AM/PM format."""
#     import datetime  # Import datetime module to get current time

#     now = datetime.datetime.now()  # Get current time
#     return now.strftime("%I:%M %p")

# def get_current_date(*args, **kwargs):
#     """Returns the current date in Month Day, Year format."""
#     import datetime
#     now = datetime.datetime.now()
#     return now.strftime("%B %d, %Y")


# # List of tools available to the agent
# tools = [
#     Tool(
#         name="Time",  # Name of the tool
#         func=get_current_time,  # Function that the tool will execute
#         # Description of the tool
#         description="Useful for when you need to know the current time",
#     ),
#     Tool(
#         name="Date",
#         func=get_current_date,
#         description="Useful for when you need to know the current date, month, or year",
#     ),
# ]

# # Pull the prompt template from the hub
# # ReAct = Reason and Action
# # https://smith.langchain.com/hub/hwchase17/react
# prompt = hub.pull("hwchase17/react")

# # Initialize a ChatOpenAI model
# llm = OllamaLLM(
#     model="llama3.2", temperature=0, base_url="https://alpaca-upright-vulture.ngrok-free.app/"
# )

# # Create the ReAct agent using the create_react_agent function
# agent = create_react_agent(
#     llm=llm,
#     tools=tools,
#     prompt=prompt,
#     stop_sequence=True,
# )

# # Create an agent executor from the agent and tools
# agent_executor = AgentExecutor.from_agent_and_tools(
#     agent=agent,
#     tools=tools,
#     verbose=True,
#     max_iterations=1
# )

# # Run the agent with a test query
# response = agent_executor.invoke({"input": "What date is it?"})

# # Print the response from the agent
# print("response:", response)


from langchain_ollama import OllamaLLM
from langchain.agents import (
    AgentExecutor,
    create_react_agent
)
from langchain_core.tools import Tool
from langchain import hub

def get_time(*args, **kwargs):
    import datetime
    now=datetime.datetime.now()
    return now.strftime("%I:%M %p")

def get_date(*args, **kwargs):
    import datetime
    now=datetime.datetime.now()
    return now.strftime("%B %d, %Y")

tools=[
    Tool(
        name="time",
        func=get_time,
        description="give the current time"
    ),
    Tool(
        name="date",
        func=get_date,
        description="give the current date"
    )
]

llm = OllamaLLM(
    model="llama3.2", temperature=0, base_url="https://alpaca-upright-vulture.ngrok-free.app/"
)

prompt=hub.pull("hwchase17/react")

agent=create_react_agent(
    tools=tools,
    llm=llm,
    prompt=prompt,
    stop_sequence=True
)

agent_executor=AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=1
)

results= agent_executor.invoke({"input":"what is the date today?"})
print(results)