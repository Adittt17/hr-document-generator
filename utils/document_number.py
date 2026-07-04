from datetime import datetime

ROMAN_MONTH = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
    11: "XI",
    12: "XII"
}

LETTER_CODE = {
    "Surat Mutasi": "MUT",
    "Surat Promosi": "PRO",
    "Surat Keterangan Kerja": "SKK"
}


def generate_document_number(letter_type, last_document_number):

    if last_document_number is None:
        sequence = 1
    else:
        sequence = int(last_document_number.split("/")[0]) + 1

    today = datetime.now()

    return (
        f"{sequence:03d}"
        f"/HC/{LETTER_CODE[letter_type]}"
        f"/{ROMAN_MONTH[today.month]}"
        f"/{today.year}"
    )