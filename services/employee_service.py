from database.supabase import supabase


def get_all_employees():

    response = (
        supabase
        .table("employee")
        .select("*")
        .order("employee_name")
        .execute()
    )

    return response.data


def get_employee(employee_id):

    response = (
        supabase
        .table("employee")
        .select("*")
        .eq("employee_id", employee_id)
        .single()
        .execute()
    )

    return response.data