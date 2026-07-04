import streamlit as st
from datetime import date, datetime

from services.employee_service import get_all_employees
from services.document_history_service import get_document_history

st.set_page_config(
    page_title="HR Document Generator",
    page_icon="📄",
    layout="wide"
)

@st.cache_data(ttl=60)
def load_data():
    employees = get_all_employees()
    documents = get_document_history()
    return employees, documents

employees, documents = load_data()

st.title("HR Document Generator")

st.markdown("""
Generate Human Capital documents automatically using employee data.

This application streamlines HR administrative processes such as employee transfers, promotions, and employment certificate generation.
""")

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Employees",
        len(employees)
    )

with col2:
    st.metric(
        "Total Documents",
        len(documents)
    )

with col3:

    today_documents = sum(
    1
    for doc in documents
    if datetime.fromisoformat(
        doc["created_at"].replace("Z", "+00:00")
    ).date() == date.today()
)

    st.metric(
        "Generated Today",
        today_documents
    )

with col4:
    st.metric(
        "Letter Templates",
        3
    )

st.divider()

left, right = st.columns([2,1])

with left:

    st.subheader("Available Documents")

    st.success("Surat Mutasi")

    st.success("Surat Promosi")

    st.success("Surat Keterangan Kerja")

with right:

    st.subheader("Technology Stack")

    st.write("• Python")
    st.write("• Streamlit")
    st.write("• Supabase")
    st.write("• python-docx")

st.divider()

st.subheader("Quick Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link(
        "pages/Generate_Letter.py",
        label="Generate Letter",
        icon="📄"
    )

with col2:
    st.page_link(
        "pages/Employee_List.py",
        label="Employee List",
        icon="👥"
    )

with col3:
    st.page_link(
        "pages/Document_History.py",
        label="Document History",
        icon="📑"
    )