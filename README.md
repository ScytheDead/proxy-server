# Python Proxy Server

This project includes a Python proxy server built with Flask that forwards all requests to the Express API server. The proxy server acts as an intermediary, facilitating communication between the Django web server and the Express API server.

## Python Version

This project requires a specific version of Python to run successfully. Ensure that you have Python installed, and the recommended version is specified below.

- Python: `>=3.9`

## Project Dependencies

- blinker v1.7.0
- certifi v2023.11.17
- charset-normalizer v3.3.2
- click v8.1.7
- Flask v3.0.0
- Flask-Cors v4.0.0
- idna v3.6
- importlib-metadata v7.0.0
- itsdangerous v2.1.2
- Jinja2 v3.1.2
- MarkupSafe v2.1.3
- python-dotenv v1.0.0
- requests v2.31.0
- urllib3 v2.1.0
- Werkzeug v3.0.1
- zipp v3.17.0

## Environment Configuration

This project utilizes a configuration file named `.env` to configuration settings. Below is an example of the content you might include in your `.env` file:

```env
PORT=60000
EXPRESS_API_BASE_URL='http://localhost:3000/api'
```

## Installation

The proxy server is configured to run on `http://localhost:60000`. To set up and run the proxy server, follow these steps:

1. Clone the repository:

  ```bash
  git clone https://github.com/ScytheDead/proxy-server.git

  cd proxy-server
  ```

1. In the project directory, create a virtual environment.

  ```bash
  python3 -m venv venv
  ```

2. Activate the virtual environment:

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

    - On Windows:

      ```bash
      .\venv\Scripts\activate
      ```

After activation, you should see the virtual environment name in your terminal prompt.

3. Install project dependencies:

  ```bash
  pip install -r requirements.txt
  ```

This ensures that the required Python packages are installed within the virtual environment.


4. Run the following command to start the Flask proxy server:

  ```bash
  python api_proxy.py
  ```

This will start the proxy server on `http://localhost:60000`, ready to forward requests.

## Note
Make sure to update the proxy server configuration or adjust the Express API server URL within the code if your Express API server is running on a different host or port.
