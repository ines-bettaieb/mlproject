import streamlit as st
from keybert import KeyBERT
# For Flair (Keybert)
from flair.embeddings import TransformerDocumentEmbeddings
import pandas as pd

doc = st.text_area(
            "Paste your text below",
            height=510,
        )

MAX_WORDS = 500
import re
res = len(re.findall(r"\w+", doc))
if res > MAX_WORDS:
            
            st.warning(
                "⚠️ Your text contains "
                + str(res)
                + " words."
                + " Only the first 500 words will be reviewed. Stay tuned as increased allowance is coming! 😊"
            )

            doc = doc[:MAX_WORDS]

submit_button = st.button(label="✨ Extractor tool!")


top_n = st.sidebar.slider("Select number of keywords to extract", 
                          1, 
                          30, 
                          10, 1,
                          help="You can choose the number of keywords/keyphrases to display. Between 1 and 30, default number is 10.")
min_ngram = st.sidebar.number_input("Min ngram", 1, 5, 1, 1)
max_ngram = st.sidebar.number_input("Max ngram", min_ngram, 5, 2, step=1)
StopWordsCheckbox = st.sidebar.checkbox(
            "Remove stop words",
            help="Tick this box to remove stop words from the document (currently English only)",
        )

use_MMR = st.sidebar.checkbox(
            "Use MMR",
            value=True,
            help="You can use Maximal Margin Relevance (MMR) to diversify the results. It creates keywords/keyphrases based on cosine similarity. Try high/low 'Diversity' settings below for interesting variations.",
        )


Diversity = st.sidebar.slider(
            "Keyword diversity (MMR only)",
            value=0.5,
            min_value=0.0,
            max_value=1.0,
            step=0.1,
            help="""The higher the setting, the more diverse the keywords.
            
Note that the *Keyword diversity* slider only works if the *MMR* checkbox is ticked.

""",
        )

if StopWordsCheckbox:
        StopWords = "english"
else:
        StopWords = None

if use_MMR:
        mmr = True
else:
        mmr = False

params = {"docs":doc,
          "top_n" : top_n,
          "keyphrase_ngram_range": (min_ngram, max_ngram),
          "stop_words": StopWords,
          "use_mmr":mmr,
          "diversity":Diversity,
          "highlight":True
          }

@st.cache_resource
def load_model():
                               
                return KeyBERT("distilbert-base-nli-mean-tokens")

kw_model = load_model()
keywords = kw_model.extract_keywords(**params)

if submit_button:
        
        st.markdown("## **🎈 Check Results **")
        df = (
    pd.DataFrame(keywords, columns=["Keyword/Keyphrase", "Relevancy"])
    .sort_values(by="Relevancy", ascending=False)
    .reset_index(drop=True)
)
        st.table(df)