import streamlit as st

from services.employee_service import (
    get_all_employees,
    get_employee
)

from services.document_service import create_document

from services.document_history_service import (
    insert_document_history,
    get_last_document_number
)

from utils.document_number import generate_document_number
from utils.date_formatter import format_date_indonesia


st.set_page_config(
    page_title="Generate Letter",
    page_icon="📄",
    layout="wide"
)

st.title("HR Document Generator")

st.divider()

# ==========================
# Employee Selection
# ==========================

employees = get_all_employees()

employee_dict = {
    f"{emp['employee_id']} - {emp['employee_name']}": emp["employee_id"]
    for emp in employees
}

letter_type = st.selectbox(
    "Letter Type",
    [
        "Surat Mutasi",
        "Surat Promosi",
        "Surat Keterangan Kerja"
    ]
)

selected_employee = st.selectbox(
    "Employee",
    list(employee_dict.keys())
)

employee = get_employee(
    employee_dict[selected_employee]
)

# ==========================
# Employee Information
# ==========================

st.divider()

st.subheader("Employee Information")

col1, col2 = st.columns(2)

with col1:

    st.text_input(
        "Employee Name",
        employee["employee_name"],
        disabled=True
    )

    st.text_input(
        "Employee ID",
        employee["employee_id"],
        disabled=True
    )

    st.text_input(
        "Department",
        employee["department"],
        disabled=True
    )

    st.text_input(
        "Position",
        employee["position"],
        disabled=True
    )

with col2:

    st.text_input(
        "Location",
        employee["location"],
        disabled=True
    )

    st.text_input(
        "Email",
        employee["email"],
        disabled=True
    )

    st.text_input(
        "Employment Status",
        employee["employment_status"],
        disabled=True
    )

    st.text_input(
        "Join Date",
        employee["join_date"],
        disabled=True
    )

# ==========================
# Document Information
# ==========================

st.divider()

st.subheader("Document Information")

last_document_number = get_last_document_number(letter_type)

document_number = generate_document_number(
    letter_type,
    last_document_number
)


st.text_input(
    "Document Number",
    value=document_number,
    disabled=True
)

effective_date = st.date_input(
    "Effective Date"
)

# ==========================
# Dynamic Form
# ==========================

if letter_type == "Surat Mutasi":

    st.divider()

    st.subheader("Transfer Information")

    new_department = st.text_input(
        "New Department"
    )

    new_position = st.text_input(
        "New Position"
    )

    new_location = st.text_input(
        "New Location"
    )

elif letter_type == "Surat Promosi":

    st.divider()

    st.subheader("Promotion Information")

    new_department = st.text_input(
        "New Department"
    )

    new_position = st.text_input(
        "New Position"
    )

    new_location = st.text_input(
        "New Location"
    )

elif letter_type == "Surat Keterangan Kerja":

    st.divider()

    st.subheader("Certificate Information")

    purpose = st.text_input(
        "Purpose"
    )

# ==========================
# Generate Document
# ==========================

st.divider()

if st.button(
    "Generate Letter",
    type="primary",
    width="stretch"
):

    form_data = {
        "document_number": document_number,
        "effective_date": format_date_indonesia(effective_date)
    }

    if letter_type == "Surat Mutasi":

        form_data["new_department"] = new_department
        form_data["new_position"] = new_position
        form_data["new_location"] = new_location

    elif letter_type == "Surat Promosi":

        form_data["new_department"] = new_department
        form_data["new_position"] = new_position
        form_data["new_location"] = new_location

    elif letter_type == "Surat Keterangan Kerja":

        form_data["purpose"] = purpose

    file_path = create_document(
        letter_type,
        employee,
        form_data
    )

    insert_document_history(
        {
            "document_number": document_number,
            "letter_type": letter_type,
            "effective_date": effective_date.isoformat(),
            "generated_by": "HR Admin",
            "file_name": file_path.name,
            "status": "Generated",
            "employee_id": employee["employee_id"]
        }
    )

    st.success("Document generated successfully!")

    with open(file_path, "rb") as file:

        st.download_button(
            "Download Word",
            data=file,
            file_name=file_path.name,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            width="stretch"
        )