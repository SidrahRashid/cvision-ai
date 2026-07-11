import fitz


def read_pdf(resume):

    pdf = fitz.open(
        stream=resume.read(),
        filetype="pdf"
    )

    resume_text = ""

    for page in pdf:
        resume_text += page.get_text()

    pdf.close()

    # Remove empty lines
    lines = resume_text.splitlines()

    lines = [line.strip() for line in lines if line.strip()]

    resume_text = "\n".join(lines)

    return resume_text