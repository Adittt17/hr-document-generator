MONTHS_ID = {
    1: "Januari",
    2: "Februari",
    3: "Maret",
    4: "April",
    5: "Mei",
    6: "Juni",
    7: "Juli",
    8: "Agustus",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "Desember",
}


def format_date_indonesia(date):
    """
    Mengubah datetime.date menjadi format:
    4 Juli 2026
    """
    return f"{date.day} {MONTHS_ID[date.month]} {date.year}"