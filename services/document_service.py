from datetime import datetime
from pathlib import Path

from utils.word_generator import generate_word
from utils.date_formatter import format_date_indonesia

# Pastikan folder generated selalu ada
OUTPUT_DIR = Path("generated")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def create_document(
    template_name,
    employee,
    form_data
):

    templates = {
        "Surat Mutasi": "templates/surat mutasi.docx",
        "Surat Promosi": "templates/surat promosi.docx",
        "Surat Keterangan Kerja": "templates/surat keterangan kerja.docx"
    }

    template_path = Path(templates[template_name])

    filename = (
        f"{employee['employee_id']}_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"
    )

    output_path = OUTPUT_DIR / filename

    data = {
        **employee,
        **form_data,
        "today": format_date_indonesia(datetime.now().date())
    }

    generate_word(
        template_path,
        output_path,
        data
    )

    return output_path