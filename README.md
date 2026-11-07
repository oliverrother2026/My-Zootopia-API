# My Zootopia API 🦊

A Python project that generates an HTML website with animal information retrieved from the API Ninjas Animals API.

## About the Project

This project was developed as part of my Masterschool Software Engineering training.

Users can search for an animal by entering its name. The application retrieves matching animal information from an external API and generates an HTML website displaying the results.

If no matching animals are found, the website displays an appropriate message.

## Features

- Search for animals by name
- Retrieve animal information from the API Ninjas Animals API
- Display animal details such as diet, location, lifespan and scientific name
- Generate an HTML website automatically
- Handle searches without matching animals
- Store the API key securely using environment variables
- Separate data fetching and website generation into different Python modules

## Technologies

- Python 3
- Requests
- Python-dotenv
- HTML
- Git and GitHub

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/oliverrother2026/My-Zootopia-API.git
cd My-Zootopia-API
```

**2. Install dependencies**

```bash
python3 -m pip install -r requirements.txt
```

**3. Configure the API key**

Create a `.env` file in the project directory:

```env
API_KEY=your_api_key_here
```

Get your own API key from https://api-ninjas.com/.

The `.env` file is excluded from Git using `.gitignore`.

## Usage

Run the website generator:

```bash
python3 animals_web_generator.py
```

Enter an animal name when prompted:

```text
Enter a name of an animal: Fox
```

The program retrieves matching animals and generates the file `animals.html`.

Open `animals.html` in your browser to view the results.

## Project Structure

```text
My_Zootopia_API/
├── animals_web_generator.py
├── data_fetcher.py
├── animals_template.html
├── animals.html
├── animals_data.json
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

**animals_web_generator.py** – Handles user input and generates the HTML website.

**data_fetcher.py** – Retrieves animal information from the API.

**animals_template.html** – HTML template used to generate the website.

**requirements.txt** – Lists the required Python packages.

**.env** – Stores the private API key locally and is not committed to GitHub.

## Author

Oliver Rother

Developed as part of the Masterschool Software Engineering program.