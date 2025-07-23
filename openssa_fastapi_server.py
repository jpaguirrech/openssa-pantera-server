#!/usr/bin/env python3
"""
Servidor OpenSSA con FastAPI y configuración de ambiente
"""

import os
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openssa import DANA, ProgramStore, Task

# Cargar variables de ambiente
def load_env():
    env_file = "environments/.env.development"
    if os.path.exists(env_file):
        with open(env_file) as f:
            for line in f:
                if line.strip() and not line.startswith('#') and '=' in line:
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value

load_env()

# Crear app FastAPI
app = FastAPI(title="OpenSSA API", version="1.0.0")

# Configurar CORS
cors_origins = os.getenv("CORS_ORIGINS", "").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos Pydantic
class QuestionRequest(BaseModel):
    question: str

class QuestionResponse(BaseModel):
    status: str
    question: str
    response: str

# Inicializar OpenSSA
try:
    ps = ProgramStore()
    dana = DANA(program_store=ps)
    print("✅ OpenSSA DANA inicializado correctamente")
except Exception as e:
    print(f"❌ Error inicializando OpenSSA: {e}")
    dana = None

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "message": "OpenSSA API is running",
        "version": "1.0.0",
        "environment": os.getenv("ENVIRONMENT", "development"),
        "port": os.getenv("OPENSSA_PORT", "8001")
    }

@app.post("/ask", response_model=QuestionResponse)
async def ask_openssa(request: QuestionRequest):
    try:
        if dana is None:
            return QuestionResponse(
                status="error",
                question=request.question,
                response="OpenSSA no está disponible"
            )
        
        task = Task(ask=request.question)
        # Aquí puedes procesar con DANA cuando esté listo
        response_text = f"Pregunta procesada por OpenSSA: {request.question}"
        
        return QuestionResponse(
            status="success",
            question=request.question,
            response=response_text
        )
    except Exception as e:
        return QuestionResponse(
            status="error",
            question=request.question,
            response=f"Error procesando pregunta: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("OPENSSA_HOST", "0.0.0.0")
    port = int(os.getenv("OPENSSA_PORT", "8001"))
    debug = os.getenv("DEBUG", "false").lower() == "true"
    
    print(f"🚀 Iniciando OpenSSA FastAPI Server")
    print(f"   - Host: {host}")
    print(f"   - Puerto: {port}")
    print(f"   - Debug: {debug}")
    print(f"   - Ambiente: {os.getenv('ENVIRONMENT', 'development')}")
    
    uvicorn.run(
        "openssa_fastapi_server:app",
        host=host,
        port=port,
        reload=debug,
        log_level="debug" if debug else "info"
    )
