from langchain_community.document_loaders import WebBaseLoader
from langchain.tools import tool
from langchain_community.document_loaders import WebBaseLoader
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

"""
webBaseLoader
"""


@tool
def webloader(query: str) -> str:
    '''
    This function is for webloader.
        Args:
            query (str): This part is used to take an url as parameter which is obtained from the google search only.
        Returns:
            str: The summerized output of the website.
    '''
    loader = WebBaseLoader(query)
    # print(loader)
    llm = ChatGroq(
        model="llama3-8b-8192",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        # other params...
    )

    # prompt = ChatPromptTemplate.from_messages(
    #     [
    #         (
    #             "system",
    #             "You are a helpful assistant that translates {input_language} to {output_language}.",
    #         ),
    #         ("human", "{input}"),
    #     ]
    # )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Your task is to summarize the content of the website.",
            ),
            ("human", "{input}"),
        ]
    )

    chain = prompt | llm
    result = chain.invoke({"input": loader.load()})
    # print(result)
    # return (loader.load())
    return result
