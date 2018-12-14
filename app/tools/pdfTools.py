from fpdf import FPDF
from flask import make_response


class PdfGenerator:
    @staticmethod
    def create_pdf_file(pdf):
        response = make_response(pdf.output(dest='S').encode('latin-1'))
        response.headers.set('Content-Disposition', 'attachment', filename='Report.pdf')
        response.headers.set('Content-Type', 'application/pdf')

        return response

    @staticmethod
    def format_pdf(data):
        date_time = 1
        issue = 2
        discipline = 3
        document = 4
        uid = 5
        project = 6
        sentiment = 7
        status = 8

        pdf = FPDF(format='A4', unit='in')
        pdf.add_page()

        effective_page_width = pdf.w - 2 * pdf.l_margin

        for item in data:
            pdf.set_font('Times', 'B', 15.0)
            pdf.cell(effective_page_width, 0.0, 'Project: {}'.format(item[project]), align='C')
            pdf.ln(0.6)
            break

        for item in data:
            pdf.set_font('Times', 'B', 10.0)
            pdf.cell(1.0, 0.0, 'ID: {} - Logged in: {}'.format(item[uid], item[date_time]))
            pdf.ln(0.15)
            pdf.cell(1.0, 0.0, 'Document: {}'.format(item[document]))
            pdf.ln(0.15)
            pdf.cell(1.0, 0.0, 'Discipline: {}'.format(item[discipline]))
            pdf.ln(0.15)
            pdf.cell(1.0, 0.0, 'Status: {}'.format(item[status]))
            pdf.ln(0.15)
            pdf.cell(1.0, 0.0, 'Sentiment: {}'.format(item[sentiment]))
            pdf.ln(0.25)

            pdf.set_font('Times', '', 10.0)
            pdf.multi_cell(effective_page_width, 0.15, item[issue])
            pdf.ln(0.5)

        return pdf
