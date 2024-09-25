from langchain_groq import ChatGroq
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.output_parsers import StrOutputParser
from react_prompt_template import get_prompt_template
from tools.google_search_tool import google_search
import warnings
import os
from dotenv import dotenv_values


def agent(query: str):
    """
        This function is used to create an reAct agent that searches the web for information.

        Args:
            query (str): The query to be passed to the agent.
        Returns:
            str: The output of the agent.
    """

    # Ignore FutureWarnings
    warnings.filterwarnings("ignore", category=FutureWarning)

    # LLM = ChatGroq(model="llama-3.1-70b-versatile")
    # This model provides unlimited limit per day
    LLM = ChatGroq(model="llama3-8b-8192")

    tools = [google_search]

    prompt_template = get_prompt_template()

    agent = create_react_agent(
        LLM,
        tools,
        prompt_template
    )

    agent_executor = AgentExecutor(
        agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

    result = agent_executor.invoke({"input": query})
    print(result["output"])
    return result["output"]


if __name__ == "__main__":
    secrets = dotenv_values(".env")
    os.environ["GROQ_API_KEY"] = secrets["GROQ_API_KEY"]
    query = input("Enter your query: ")
    agent(query)
