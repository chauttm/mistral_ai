How to create the first chat box using Mistral AI (free API key)
0. create a new folder for your project

1. create a virtual environment from inside the project's folder using terminal
python -m venv .venv

2. start virtual environment

.\.venv\Scripts\activate

or if you're using a Linux machine

source .venv\Scripts\activate

From now on, always start virtual environment before running/installing anything

3. Install libraries
pip install streamlit mistralai python-dotenv

4. obtain api key from
https://console.mistral.ai/

5. Create a .env file in your root project folder to securely store your key
MISTRAL_API_KEY=your_actual_api_key_here

6. Create the app, say app.py 

7. Run the app at the terminal prompt
streamlit run app.py

you should see something like this
2026-08-03 23:46:29.948 Uvicorn server started on :::8501

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://10.2.0.2:8501

That's it! Have fun!