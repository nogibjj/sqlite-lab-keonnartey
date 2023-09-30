import requests
import os

def extract(
    url="https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv",
    file_path="/data/Diabetes.csv",
    directory="data"
):
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    
    # Join the directory and file name to get the full path
    full_file_path = os.path.join(directory, 'Diabetes.csv')
    
    # Check if the file already exists
    if os.path.exists(full_file_path):
        print(f"File '{full_file_path}' already exists.")
        return full_file_path

    # Fetch the content from the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Write the content to the file
        with open(full_file_path, "wb") as f:
            f.write(response.content)
        print(f"File '{full_file_path}' extracted successfully.")
    else:
        print(f"Failed to fetch content from URL. Status code: {response.status_code}")
    
    return full_file_path

# Example usage
extract()
