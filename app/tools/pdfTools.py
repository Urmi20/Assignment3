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
        pdf = FPDF(format='A4', unit='in')
        pdf.add_page()

        effective_page_width = pdf.w - 2 * pdf.l_margin

        for item in data:
            pdf.set_font('Times', 'B', 15.0)
            pdf.cell(effective_page_width, 0.0, 'Project: {}'.format(item.get('project')), align='C')
            pdf.ln(0.6)
            break

        for item in data:
            pdf.set_font('Times', 'B', 10.0)
            pdf.cell(1.0, 0.0, 'ID: {} - Logged in: {}'.format(item.get('id'), item.get('date_added')))
            pdf.ln(0.15)
            pdf.cell(1.0, 0.0, 'Document: {}'.format(item.get('document')))
            pdf.ln(0.15)
            pdf.cell(1.0, 0.0, 'Discipline: {}'.format(item.get('discipline')))
            pdf.ln(0.15)
            pdf.cell(1.0, 0.0, 'Status: {}'.format(item.get('status')))
            pdf.ln(0.15)
            pdf.cell(1.0, 0.0, 'Sentiment: {}'.format(item.get('sentiment')))
            pdf.ln(0.25)

            pdf.set_font('Times', '', 10.0)
            pdf.multi_cell(effective_page_width, 0.15, item.get('description'))
            pdf.ln(0.5)

        return pdf
