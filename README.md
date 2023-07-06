# streamlit-and-OpenAI
## OpenAI API:
OpenAI API is a powerful tool developed by OpenAI that allows developers to access and utilize the capabilities of the GPT-3 language model. GPT-3, which stands for "Generative Pre-trained Transformer 3," is an advanced deep learning model that excels in natural language processing tasks. By integrating the OpenAI API into their applications, developers can leverage the power of GPT-3 to generate human-like text, perform language translation, answer questions, create conversational agents, and much more.

The OpenAI API provides a straightforward interface for making requests to the model. Developers can send a prompt or a series of instructions to the API and receive the model's generated response. The API supports various programming languages and frameworks, making it flexible and accessible for developers from different backgrounds.

## Streamlit:
Streamlit is an open-source Python library that simplifies the process of building interactive and data-driven web applications. With Streamlit, developers can quickly create and deploy web apps without the need for extensive web development knowledge. It focuses on ease of use, allowing developers to write simple Python scripts to create web interfaces and visualize data.

Streamlit provides a wide range of features, including widgets for user input, interactive visualizations, and real-time updates. Developers can easily incorporate machine learning models, data analysis, and other functionalities into their Streamlit apps. The resulting apps can be deployed locally or hosted on cloud platforms, enabling easy sharing and collaboration.

The combination of OpenAI API and Streamlit opens up exciting possibilities for building intelligent and interactive applications. Developers can utilize the power of GPT-3 through the OpenAI API to enhance the capabilities of their Streamlit apps. They can create chatbots, generate dynamic content, provide natural language interfaces, and create engaging user experiences.

Overall, OpenAI API and Streamlit are powerful tools that, when used together, enable developers to build sophisticated applications with advanced natural language processing capabilities, interactive user interfaces, and data visualization. This combination empowers developers to create innovative solutions and enhance user experiences in various domains.



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
