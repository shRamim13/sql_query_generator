# SQL Query Generator Using LLMs 🌟

Welcome to the **SQL Query Generator** project! This tool leverages the power of Large Language Models (LLMs) to transform natural language questions into SQL queries and retrieve data from a SQLite database. Perfect for anyone who wants to interact with databases without needing to know SQL!

## 🚀 Features
- **Natural Language to SQL**: Enter your questions in plain English, and watch the magic as they are converted into SQL queries.
- **Streamlit Interface**: A user-friendly web interface built with Streamlit, making it easy to interact with the database.
- **Extensive Prompts**: The system is trained with detailed and varied prompts to handle a wide range of questions.
- **Real-Time Query Results**: Instantly see the results of your SQL queries displayed in a beautiful, interactive table.

## 📋 Requirements

- **Python Version**: 3.9 or higher
- **Libraries**: All required libraries are listed in the `requirements.txt` file. Install them using:
  ```bash
  pip install -r requirements.txt
API Key: You'll need a Google API key stored in a .env file for the Generative AI model. You can also set it directly in the script.
🛠️ Setup
Install Python: Ensure Python 3.9+ is installed on your system.
Install Dependencies: Run the following command to install the required packages:
bash
Copy code
pip install -r requirements.txt
Create the Database: Generate the SQLite database by running the sqlite.py script:
bash
Copy code
python sqlite.py
This will create a student.db file, which the application will use.
Configure API Key: Add your Google API key to a .env file in the root directory:
makefile
Copy code
GOOGLE_API_KEY=your_google_api_key_here
Alternatively, you can set the API key directly in the sql.py script.
Run the Application: Start the Streamlit app by running:
bash
Copy code
streamlit run sql.py
🧑‍💻 Usage
Simply open the Streamlit interface in your browser, input your question, and let the model generate the SQL query and retrieve the data for you. It’s that easy!

🤝 Contributing
Feel free to fork this repository, make improvements, and submit a pull request. Contributions are always welcome!

🌍 Message
From the river to the sea, Palestine will be free.



📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

Happy Learning with LLMs! 🎉