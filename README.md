# Wikipedia Scraper Microservice

This is a simple Microservice that scrapes Wikipedia for information about a given topic. It is written in Python v3.9.7. It uses `FastAPI` for the API, `wikipedia` library by Jonathon Goldsmith for the scraping, and `uvicorn` for the server.

## Installation

To install the dependencies, run the following command:
```
pip install -r requirements.txt
```
It's highly recommended to use a virtual environment.
Learn more about virtual environments [here](https://docs.python.org/3/tutorial/venv.html).

## Running the server

To run the server, run the following command:
```
uvicorn main:app --reload
```
This will start the server on `localhost:8000`. `--reload` is optional and will reload the server on any changes to the code.  You can change the port by adding `--port <port_number>` to the command.

## Usage

To use the API, simply send a `GET` request to the /wiki endpoint with the topic you want to search for as a query parameter.

### Endpoints

```
GET /wiki/{topic}/summary
```
```
GET /wiki/{topic}/{section}/
```
```
GET /wiki/{topic}/images/
```
```
GET /wiki/{topic}/content/
```
```
GET /wiki/{topic}/categories/
```

### Example

```
GET /wiki/taylorswift/summary
This will return a summary of the Taylor Swift Wikipedia page.
```
```
GET /wiki/taylorswift/wealth
This will return the wealth section of the Taylor Swift Wikipedia page.
```
```
GET /wiki/taylorswift/images
This will return a list of images on the Taylor Swift Wikipedia page.
```
```
GET /wiki/taylorswift/content
This will return the full content of the Taylor Swift Wikipedia page.
```
```
GET /wiki/taylorswift/categories
This will return a list of categories on the Taylor Swift Wikipedia page.
```

### Bugs

There are a few bugs that I am aware of. If you find any that prevent the microservice from working for your use case, please let me know as soon as possible.