from langchain.agents import tool
from googlesearch import search


@tool
def google_search(query: str, num_results: int = 5):
    """
    A tool to search a query from Google.

    Args:
        query (str): The search query string.
        num_results (int): Number of search results to return. (default: 5)

    Returns:
        list: A list of URLs from Google search results.
    """
    search_results = []
    try:
        # Perform Google search and store the results
        for result in search(query, num_results):
            search_results.append(result)
    except Exception as e:
        return f"Error occurred: {str(e)}"

    return search_results


# Test the tool
# if __name__ == "__main__":
#     # Example usage
#     query = "LangChain documentation"
#     results = google_search(query, num_results=10)
#     print(results)
