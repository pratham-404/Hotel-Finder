# Hotel Finder 👀🏨

Hotel Finder is a simple Flask web application that allows users to search for hotels in a given location within a certain radius. The application searches for hotels and returns the name, address, and rating of each hotel found.

## Deployment 🚀
The app is deployed at [link](https://hotel-finder-kw9i.onrender.com/). You can use the search form on this page to find hotels.

## Requirements 📋

To run Hotel Finder, you will need the following:

- Python 3.6 or higher 🐍
- Flask 🌶️
- Requests 🌐

## Installation 💻

1. Clone the repository:

```
    git clone https://github.com/pratham-404/Hotel-Finder.git
```

2. Install the required packages:

```
    pip install -r requirements.txt
```

## Usage 🛠️

To start the application, run the following command:
```
    python app.py
```
Once the application is running, you can access it by visiting `http://localhost:5000` in your web browser.


### API Endpoints 📡

#### GET /search 🔍

The `/search` endpoint allows you to search for hotels in a given location within a certain radius. To use this endpoint, send a GET request to `/search` with the following parameters:

- `location`: The location you want to search for hotels in (required).
- `radius`: The radius in meters within which to search for hotels (optional).

The endpoint returns a JSON object containing an array of hotels found in the search, along with their name, address, and rating. The object is of the following format:

#### Examples 🌟

1. Location: Matunga, Mumbai

```bash
https://hotel-finder-kw9i.onrender.com/search?location=Matunga,Mumbai
```
Output: [click](https://hotel-finder-kw9i.onrender.com/search?location=Matunga,Mumbai) 🌞

2. Location: Matunga, Mumbai & Radius: 10 Km

```bash
https://hotel-finder-kw9i.onrender.com/search?location=Matunga,Mumbai&radius=10
```
Output: [click](https://hotel-finder-kw9i.onrender.com/search?location=Matunga,Mumbai&radius=10) 🌞

## Contributing 🤝
Contributions to Hotel-Finder are welcome! If you'd like to contribute, please create a pull request with your proposed changes. 👨‍💻

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
