How to create the first chat box using Mistral AI (free API key)

#### 0. Create a new folder for your project
Optional, start a git repository there

#### 1. Create a virtual environment from inside the project's folder using terminal
<code>python -m venv .venv</code>

#### 2. start virtual environment

<code> .\\.venv\Scripts\activate</code>

or if you're using a Linux machine

<code>source .venv/Scripts/activate</code>

From now on, always start virtual environment before running/installing anything

#### 3. Install libraries
<code>pip install streamlit mistralai python-dotenv</code>

#### 4. obtain api key from https://console.mistral.ai/

#### 5. Create a .env file in your root project folder to securely store your key
<code>MISTRAL_API_KEY=your_actual_api_key_here</code>

#### 6. Create the app, say app.py 

#### 7. Run the app at the terminal prompt
<code>streamlit run app.py</code>

you should see something like this
<code>
2026-08-03 23:46:29.948 Uvicorn server started on :::8501

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://10.2.0.2:8501
</code>
That's it! Have fun!