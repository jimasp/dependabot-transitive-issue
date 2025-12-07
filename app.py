"""
Simple application using requests to demonstrate Dependabot transitive dependency issue.
"""
import requests


def fetch_data(url):
    """Fetch data from a URL using requests."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


if __name__ == '__main__':
    # Example usage
    url = "https://api.github.com/repos/python/cpython"
    data = fetch_data(url)
    if data:
        print(f"Repository: {data.get('name')}")
        print(f"Stars: {data.get('stargazers_count')}")
