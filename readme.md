# Key Extractor tool with KeyBert and Streamlit
- This Streamlit application uses KeyBert to extract meaningful keywords from text documents.
- KeyBert can be an alternative to bag of words techniques (e.g. Count or Tfidf vectorizers) that might suffer from noisy results.
- KeyBert uses a minimal keyword extraction technique that leverages multiple NLP embeddings and relies on Transformers 🤗 to create keywords/keyphrases that are most similar to a document.

## Installation

1. Create a project repository:
```bash 
mkdir key-word-extractor
```
2. Navigate to the project directory:
```bash 
cd key-word-extractor
```
3. Create and activate a virtual environment (optional but recommended):
```bash
python3 -m venv venv source venv/bin/activate
```
4. Install the dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
streamlit run main.py
```
2. Access the app in your browser at [http://localhost:8501](http://localhost:8501).

3. You will see a text input field where you can copy/paste your text.

4. Utilize the left-hand panel to experiment with settings and visualize dynamic result changes.

5. To exit the app, press `Ctrl+C` in the terminal.

## Screenshots

![title](Outputs/Output1.png)


