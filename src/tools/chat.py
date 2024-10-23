from langchain_community.document_loaders import WebBaseLoader
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


@tool
def general_purpose_chat(prompt: str) -> str:
    '''
    This function is for general purpose chatting with the AI.
        Args:
            prompt (str): 
        Returns:
            str: The chat result.
    '''

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
                "You are a helpful assistant.",
            ),
            ("human", "{input}"),
        ]
    )

    chain = prompt | llm
    result = chain.invoke({"input": prompt})
    return result
