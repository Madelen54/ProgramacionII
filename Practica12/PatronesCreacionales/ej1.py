class IExportador:
    def exportar(self, documento: str):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")
class ExportadorPDF(IExportador):
    def exportar(self, documento: str):
        print(f"Exportando documento a PDF: '{documento[:30]}...' (formato binario/complejo)")

class ExportadorDOCX(IExportador):
    def exportar(self, documento: str):
        print(f"Exportando documento a DOCX: '{documento[:30]}...' (formato XML/estructurado)")

class ExportadorTXT(IExportador):
    def exportar(self, documento: str):
        print(f"Exportando documento a TXT: '{documento[:30]}...' (texto plano)")
class FabricaExportadores:
    def crear_exportador(self) -> IExportador:
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

class FabricaPDF(FabricaExportadores):
    def crear_exportador(self) -> IExportador:
        return ExportadorPDF()

class FabricaDOCX(FabricaExportadores):
    def crear_exportador(self) -> IExportador:
        return ExportadorDOCX()

class FabricaTXT(FabricaExportadores):
    def crear_exportador(self) -> IExportador:
        return ExportadorTXT()
class EditorTexto:
    def __init__(self, fabrica_inicial: FabricaExportadores):
        self._fabrica = fabrica_inicial

    def establecer_fabrica(self, nueva_fabrica: FabricaExportadores):
        self._fabrica = nueva_fabrica
        print(f"Fábrica de exportadores cambiada a: {self._fabrica.__class__.__name__}")

    def exportar_documento(self, contenido: str):
        print("\nSolicitando exportación...")
        exportador = self._fabrica.crear_exportador()
        exportador.exportar(contenido)
        print("Exportación finalizada.")

if __name__ == "__main__":
    mi_documento = "Este es un documento de ejemplo que contiene texto para ser exportado a diferentes formatos."
    editor = EditorTexto(FabricaPDF())
    editor.exportar_documento(mi_documento)
    editor.establecer_fabrica(FabricaDOCX())
    editor.exportar_documento(mi_documento)

    editor.establecer_fabrica(FabricaTXT())
    editor.exportar_documento(mi_documento)
