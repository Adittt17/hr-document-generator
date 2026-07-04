from database.supabase import supabase


def insert_document_history(data):

    response = (
        supabase
        .table("document_history")
        .insert(data)
        .execute()
    )

    return response.data


def get_document_history():

    response = (
        supabase
        .table("document_history")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )

    return response.data


def get_last_document_number(letter_type):

    response = (
        supabase
        .table("document_history")
        .select("document_number")
        .eq("letter_type", letter_type)
        .order("created_at", desc=True)
        .limit(1)
        .execute()
    )

    if len(response.data) == 0:
        return None

    return response.data[0]["document_number"]