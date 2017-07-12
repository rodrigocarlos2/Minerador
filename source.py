import pdfminer
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.pdfdevice import TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from pdfminer.utils import set_debug_logging
import io

class LeitorPdf():
    def __init__(self, **kwargs):
        self.resource_manager = PDFResourceManager(caching=False)
        self.output_stream = io.StringIO()
        self.device = TextConverter(self.resource_manager, self.output_stream, laparams=None)

    def extrair_texto(self, file_name):
        fp = io.open(file_name, 'rb')
        process_pdf(self.resource_manager, self.device, fp, set(), maxpages=0, password='', caching=False, check_extractable=True)
        return self.output_stream.getvalue()


texto = LeitorPdf().extrair_texto('qos.pdf')
print(texto)
