# SailPointHACK

Welcome to the SailPointHACK repository! This project is designed to help you get started with the SailPoint IdentityNow API using Python. It provides a simple example of how to interact with the API to find and retrieve identity information. This repository is intended to serve as a starting point for a hackathon, where engineers with little to no experience with the SailPoint API and Python can quickly get up to speed and start building their own solutions.

## Project Structure

- **api_connection.py**: Contains functions to obtain access tokens and create connection headers.
- **me.py**: Script to find and retrieve identity information based on the provided first and last name.
- **.env**: Environment variables for API credentials and base URL.
>[!NOTE]
> `.env` files are used to store environment variables in key-value pairs for applications, helping manage configuration settings without hardcoding them into source code. They enhance security by keeping sensitive information like API keys and database credentials out of version control systems
- **README.md**: Project documentation.

## Prerequisites for Hackathon

- Install Visual Studio Code 
- Install Python 3.13 
>[!NOTE]
>If you'd like to get a headstart on some Python fundamentals try [this Codecademy course](https://www.codecademy.com/learn/learn-python-3).
- Install Postman 
- License for Github CoPilot
- Think of something that would make your job easier when SailPoint is Live. Don't worry if it sounds complex because we can always focus on one part of it on the day then develop the rest of it outside the hackathon. 
 
## Setup

1. Clone the repository.
2. Create a `.env` file in the root directory with the following content:
    ```env
    CLIENT_ID={your_client_id}
    CLIENT_SECRET={your_client_secret}
    BASE_URL=https://tenantname.api.identitynow.com/
    CERT_PATH=path/to/your/cert.pem
    NAME="Firstname Lastname"
    ```
> [!NOTE] 
> You only need to configure CERT_PATH if your organization uses SSL/TLS inspection on its firewalls.

## Usage

### Find Identity

To find and retrieve identity information based on the provided first and last name, run the following command:
```sh
python me.py
```
The script will:

- Set up logging to record the process.
- Load environment variables from the `.env` file.
- Obtain an access token using the credentials provided.
- Use the SailPoint IdentityNow API to search for the identity based on the first and last name.
- Save the retrieved identity information to a file named `identity.json`.

## Logging

Logs are stored in the `logs` directory. Each script creates its own log file with detailed information about the execution, including any errors encountered during the process.

## Detailed Explanation

### api_connection.py

This file handles the connection to the SailPoint IdentityNow API. It includes functions to set up logging, load environment variables, and obtain an access token. The `get_api_connection` function creates the necessary headers for API requests, which include the access token. You can use these functions in your final product to handle authentication and API connections.

### me.py

This script demonstrates how to find and retrieve identity information using the SailPoint IdentityNow API. It includes:

- **Logging**: Sets up logging to record the process and any errors.
- **Environment Variables**: Loads environment variables from the `.env` file.
- **API Connection**: Uses the `get_api_connection` function to create headers for API requests.
- **Find Identity**: Searches for an identity based on the provided first and last name and saves the retrieved information to a file named `identity.json`.