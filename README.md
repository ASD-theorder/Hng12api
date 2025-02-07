# Hng12api
This is a simple public API built with **FastAPI** that returns the following information:
- My registered email address.
- The current datetime (in ISO 8601 format).
- The URL to my project's GitHub repository.
I designed it for the HNG12 internship challenge. I want to use it show my knowledge of backend(run your tests). You can follow the following instructions to create yours.

**Live API URL**
[https://hng12api-ansp.onrender.com]

## Setup Instructions
- Create a new folder and name it eg basicapi
- Open your command prompt (Win + R, type cmd then press enter)
- Run
cd Desktop\basicapi (if you created the folder in desktop, if it's in a different location eg documents, change it to Documents\basicapi)
- Then check if you're inside the correct directory by running
cd
you should see C:\Users\HP\Desktop\basicapi

- Make sure you have the lastest **Python 3.8+** and *pip* installed. You can check the version by running:
```bash
python --version
pip --version
```
If you have, you should see something like this
```bash
Python 3.x.x
```
If you get an error like"not recognized as an internal or external command", you need to install python

- Install Dependencies:Run the following in your terminal

1. Clone the repository
```bash
git clone https://github.com/ASD-theorder/Hng12api.git
```

2. Navigate to the project directory:
```bash
cd Hng12api
```

3. Create a virtual environment (recommended):
```bash
python -m venv venv
```

4. Activate the virtual environment:

On Windows:

```bash
venv\Scripts\activate
```
On MacOS/Linux:

```bash
source venv/bin/activate
```


5. Install required dependencies:
```bash
pip install -r requirements.txt
```

- Run the Project Locally

Start the FastAPI server:
```bash
uvicorn main:app --reload
```
The API should now be running at http://127.0.0.1:8000/

## API Documentation

### Endpoint URL
The API endpoint is a *GET* request to the root URL /

GET http://127.0.0.1:8000/

### Request Format
- *Method*: GET
- *Headers*: None required.
- *Body*: No body is needed.

### Response Format
When you make a successful `GET` request to the API,the API will respond with a **JSON** object containing three fields: email, current_datetime, and github_url.

```json
{
   "email": 
"abele4336@gmail.com",
    "current_datetime": 
"2025-02-06T09:30:00Z",
    "github_url": 
"https://github.com/ASD-theorder/Hng12api.git"
}
```

## Example Usage

To interact with the API, simply visit the endpoint in your browser or use a tool like Postman or cURL.

For example, using Web browser:

Copy this link http://127.0.0.1:8000/ and run in browser

This will return a response like:

```json
{
    "email": 
"abele4336@gmail.com",
    "current_datetime": 
"2025-02-06T09:30:00Z",
    "github_url": 
"https://github.com/ASD-theorder/Hng12api.git"
}
```
It will return the same response for the live API
[https://hng12api-ansp.onrender.com]

If you're interested in hiring Python developers, check out this link:

[Python Developers](https://hng.tech/hire/python-developers)