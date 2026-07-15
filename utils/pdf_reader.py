import fitz


def read_pdf(resume):

    try:

        pdf = fitz.open(
            stream=resume.read(),
            filetype="pdf"
        )

        text = ""

        for page in pdf:

            page_text = page.get_text()

            if page_text:

                text += page_text + "\n"

        pdf.close()

        return text.strip()

    except Exception as e:

        print("\n========== PDF ERROR ==========")
        print(e)
        print("================================\n")

        return ""