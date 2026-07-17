from pathlib import Path
from pypdf import PdfWriter


def combine_pdfs(pdf_files: list[str], output_file: str) -> None:
    writer = PdfWriter()

    try:
        for pdf_file in pdf_files:
            pdf_path = Path(pdf_file)

            if not pdf_path.exists():
                raise FileNotFoundError(f"File not found: {pdf_path}")

            writer.append(str(pdf_path))

        with open(output_file, "wb") as output_pdf:
            writer.write(output_pdf)

        print(f"PDFs combined successfully: {output_file}")

    finally:
        writer.close()


combine_pdfs(
    pdf_files=[
        r"C:\Temp\input_1.pdf",
        r"C:\Temp\input_2.pdf",
    ],
    output_file=r"C:\Temp\combined_output.pdf",
)
