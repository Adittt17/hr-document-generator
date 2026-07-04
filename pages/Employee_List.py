import streamlit as st
import pandas as pd

from services.employee_service import get_all_employees

st.title("Employee List")

employees = get_all_employees()

df = pd.DataFrame(employees)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)