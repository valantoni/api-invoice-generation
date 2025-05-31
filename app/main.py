from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from jinja2 import Environment, FileSystemLoader
import tempfile
from weasyprint import HTML

app = FastAPI()

# Configurar Jinja2 para cargar plantillas
TEMPLATES_DIR = "/templates"
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
template = "invoicev1.html"

# 📦 Modelo de datos para la factura
class FacturaData(BaseModel):
    cliente: str
    direccion: str
    concepto: str
    importe: float
    fecha: str
    numero_factura: str

@app.post("/factura/pdf")
def generar_factura(factura: FacturaData):
    try:
        # Renderizar HTML usando Jinja2
        template = env.get_template("factura.html")
        html_content = template.render(factura=factura)

        # Generar PDF usando WeasyPrint
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            HTML(string=html_content).write_pdf(tmp.name)
            tmp.seek(0)
            return StreamingResponse(open(tmp.name, "rb"), media_type="application/pdf", headers={
                "Content-Disposition": f"inline; filename=factura_{factura.numero_factura}.pdf"
            })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar la factura: {str(e)}")
