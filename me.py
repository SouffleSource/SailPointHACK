# Import necessary libraries
import os
import json
import requests
import logging
from dotenv import load_dotenv
from api_connection import get_api_connection

# Function to set up logging
def setup_logging():
    # Check if 'logs' directory exists, if not, create it
    if not os.path.exists('logs'):
       os.makedirs('logs')
    # Create a logger object
    logger = logging.getLogger('me')
    # Set the logging level to INFO
    logger.setLevel(logging.INFO)
    # Create a file handler to write log messages to a file
    handler = logging.FileHandler('logs/me.log')
    # Define the format for the log messages
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    # Set the formatter for the handler
    handler.setFormatter(formatter)
    # Add the handler to the logger
    logger.addHandler(handler)
    # Return the logger object
    return logger

# Set up logging and store the logger object in a variable
logger = setup_logging()
# Log a message indicating that logging setup is complete
logger.info("Logging setup complete.")

# Load environment variables from a .env file
load_dotenv()
# Get the values of the environment variables and set them as strings so they can be used in the script
cert_path = os.getenv("CERT_PATH")
base_url = os.getenv('BASE_URL')
name = os.getenv('NAME')
# Construct the authentication URL using the base URL string
identities_url = f"{base_url}beta/identities"
headers = get_api_connection()

# Ensure all required environment variables are set
if not all([base_url, cert_path, name]):
    # Log an error message if any environment variable is missing
    logger.error("Missing one or more required environment variables.")
    # Raise an error to stop the program
    raise EnvironmentError("Missing one or more required environment variables.")

# Function to find an identity based on the provided first and last name
def find_identity():
    # Split the name into first name and last name
    firstname, lastname = name.split()
    # Create a filter string to search for the identity
    filters = f"firstname eq \"{firstname}\" and lastname eq \"{lastname}\""
    try:
        # Send a GET request to the identities endpoint with the filters
        response = requests.get(f"{identities_url}?filters={filters}", headers=headers, verify=cert_path)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the response JSON to get the list of identities
            identities = response.json()
            # Check if any identities were found
            if identities:
                # Get the first identity from the list
                identity = identities[0]
                # Log a success message with the found identity
                logger.info(f"Found identity: {identity}")
                # Return the found identity
                return identity
            else:
                # Log a message if no matching identity was found
                logger.info("No matching identity found.")
                return None
        else:
            # Log an error message if the request failed
            logger.error(f"Failed to retrieve identities. Status code: {response.status_code}")
            logger.error(f"Response content: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        # Log an error message if an exception occurred during the request
        logger.error(f"Exception occurred while retrieving identities: {e}")
        return None

# Main block to execute the script
if __name__ == "__main__":
    # Call the find_identity function to search for the identity
    identity = find_identity()
    # Check if an identity was found
    if identity:
        # Open a file named 'identity.json' in write mode
        with open('identity.json', 'w') as f:
            # Write the found identity to the file in JSON format
            json.dump(identity, f, indent=4)
        # Print a success message
        print("Identity found and saved to identity.json")
    else:
        # Print a message if no matching identity was found
        print("No matching identity found.")