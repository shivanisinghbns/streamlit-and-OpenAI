# Chatbot for Hospital Information

This chatbot is designed to provide information about the top 50 hospitals. It utilizes web scraping techniques to gather data from a website, interacts with an API to obtain additional information, and presents the results through a Streamlit-based frontend.

## How it Works

1. **Web Scraping**: The chatbot employs the `requests` library to scrape the necessary data from a website. It targets the top 50 hospitals and extracts relevant information such as hospital names, rank and its country.

2. **CSV Agent**: The scraped data is then stored in a CSV file, making it easily accessible for further processing and retrieval.

3. **API Integration**: Used open ai api key and csv_agent to generate response. 

4. **Streamlit Frontend**: The chatbot's frontend is built using Streamlit, a Python library for creating interactive web applications. It provides a user-friendly interface for users to interact with the chatbot and obtain hospital information.

## Usage

- When the chatbot interface loads, you will be prompted to enter a query.
- Type your question or request for hospital information and press Enter.
- The chatbot will process your input and display the relevant details about hospitals.
- You can continue to ask questions and explore different hospital information.

## Limitations

- The chatbot's dataset is limited to the top 50 hospitals. Therefore, it may not provide information about hospitals beyond this list.
