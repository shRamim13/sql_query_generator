🌟 SQL Query Generator Using LLMs
Welcome to the SQL Query Generator project! This tool harnesses the power of Large Language Models (LLMs) to seamlessly transform your natural language questions into SQL queries, retrieving the data you need from a SQLite database—all through an intuitive and user-friendly interface.

🚀 Features
Natural Language to SQL: Effortlessly convert plain English questions into SQL queries with precision.
Streamlit-Powered Interface: Interact with your database through a sleek and responsive web interface.
Robust Prompt Engineering: Equipped with extensive prompts to handle a diverse array of queries.
Real-Time Query Execution: Instantly view results in a well-organized, interactive table.
📋 Requirements
Python Version: 3.9 or higher
Dependencies: Install all necessary libraries using:
bash
Copy code
pip install -r requirements.txt
API Key: Secure a Google API key, stored in a .env file, for the Generative AI model. Alternatively, configure it directly in the code.
🛠️ Setup Guide
Create a Conda Environment: Start by creating a new Conda environment with Python 3.10:

bash
Copy code
conda create -p nenv python==3.10 -y
Activate your environment:

bash
Copy code
conda activate ./nenv
Install Dependencies: With the environment activated, install all required packages:

bash
Copy code
pip install -r requirements.txt
Create the Database: Generate the SQLite database by running:

bash
Copy code
python sqlite.py
This command creates the student.db file, which the application will use.

Configure Your API Key: Store your Google API key in a .env file:

env
Copy code
GOOGLE_API_KEY=your_google_api_key_here
Or, directly set the API key in the sql.py script.

Launch the Application: Start the Streamlit app with:

bash
Copy code
streamlit run sql.py
🧑‍💻 Usage Instructions
Open the Streamlit Interface: Launch the app in your browser.
Ask Your Question: Type your natural language question and let the model generate the SQL query.
View Results: Instantly see your query results displayed in a clean, interactive table.
🌍 Support & Contribution
We welcome all contributions! Whether it’s improving the code, adding new features, or refining the interface, your input is valuable. Fork this repository, make your changes, and submit a pull request.

📄 License
This project is licensed under the MIT License. For more details, see the LICENSE file.

Happy Learning with LLMs! 🎉
