# SQL Query Generator Using LLMs 🌟

Welcome to the **SQL Query Generator** project! This tool leverages the power of Large Language Models (LLMs) to transform natural language questions into SQL queries and retrieve data from a SQLite database. Perfect for anyone who wants to interact with databases without needing to know SQL!

## Features

- Convert English questions to SQL queries.
- Streamlit interface for easy interaction.
- Real-time query execution and results display.

## Requirements

- Python 3.9+
- Dependencies: `pip install -r requirements.txt`
- Google API Key (store in `.env` or set directly in the code)

## Setup & Run

  1. **Create Conda Environment**:
     ```bash
     conda create -p nenv python==3.10 -y
     conda activate ./nenv
  2. **Install Dependencies**:
     ```bash
     pip install -r requirements.txt
  3. **Create Database**:
     ```bash
     python sqlite.py
  4. **Configure API Key**:

     Create a `.env` file with:
      ```env
      GOOGLE_API_KEY=your_google_api_key_here  
  5. **Run the Application**:
      ```bash
      streamlit run sql.py
      
## Usage

1. Open the Streamlit app in your browser.
2. Enter a natural language question.
3. View the generated SQL query and results in an interactive table.

## Contribution

Feel free to fork the repository, make improvements, and submit a pull request.

## License

MIT License. See LICENSE for details.

Happy Learning with LLMs! 🎉

---

**From the River to the Sea, Palestine will be free**


                  
