import pandas as pd
import streamlit as st

from services.document_history_service import get_document_history

st.title("Document History")

history = get_document_history()

df = pd.DataFrame(history)

st.dataframe(
    df,
    width="stretch",
    hide_index=True
)