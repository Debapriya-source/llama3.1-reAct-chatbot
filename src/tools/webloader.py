from langchain_community.document_loaders import WebBaseLoader
from langchain.tools import tool

"""
webBaseLoader
"""

@tool
def webloader(query: str) ->str :
    '''
    This function is for webloader.
        Args:
            query (str): This part is used to take an url as parameter..
        Returns:
            str: The output of the website.
    '''
    loader = WebBaseLoader(query)
    print(loader)
    return(loader.load())
