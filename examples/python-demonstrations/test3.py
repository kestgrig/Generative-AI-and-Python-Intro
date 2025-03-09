# Step 1: Import the requests module to make HTTP requests
import requests

# Step 2: Define a function to fetch and display todo items
def fetch_todos():
    # Step 3: Define the API URL where todos are available
    url = "https://jsonplaceholder.typicode.com/todos"
    
    try:
        # Step 4: Send a GET request to fetch data from the API
        response = requests.get(url)

        # Step 5: Raise an error if the request fails (e.g., 404, 500 errors)
        response.raise_for_status()
        
        # Step 6: Convert the response JSON data into a Python list
        todos = response.json()

        # Step 7: Loop through the first 10 todos and print their details
        for todo in todos[:10]:  # Extracts the first 10 items
            print(f"ID: {todo['id']}, Title: {todo['title']}, Completed: {todo['completed']}")

    except requests.exceptions.RequestException as e:
        # Step 8: Handle any errors that occur during the request
        print(f"Error fetching data: {e}")

# Step 9: Execute the function only if this script is run directly
if __name__ == "__main__":
    fetch_todos()