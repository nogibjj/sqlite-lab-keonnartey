"""
Extract a dataset from a URL like Kaggle or data.gov. 
JSON or CSV formats tend to work well
"""

import requests
import os

def extract(
    url="https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv",
    file_path="/data/Diabetes.csv",
    directory="data"
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
