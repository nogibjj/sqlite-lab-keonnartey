import requests



def extract(
    url="https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv",
    file_path="Diabetes.csv",
):
    """Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
import requests
