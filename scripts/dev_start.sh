#!/bin/bash

echo "🚀 Iniciando OpenSSA FastAPI en modo desarrollo..."

# Cargar ambiente de desarrollo
source /home/ubuntu/pantera-test1-workspace/scripts/load_env.sh development

# Activar entorno virtual
source /home/ubuntu/openssa-env/bin/activate

# Navegar al directorio del proyecto
cd /home/ubuntu/pantera-test1-workspace

# Verificar OpenSSA
python3 -c "import openssa; print(f'✅ OpenSSA version: {openssa.__version__}')" || {
    echo "❌ Error: OpenSSA no disponible"
    exit 1
}

echo "🔥 Servidor FastAPI con auto-reload en puerto 8001..."
echo "   Health Check: http://3.131.95.194:8001/health"
echo "   API Docs: http://3.131.95.194:8001/docs"
echo "   Presiona Ctrl+C para detener"
echo ""

# Iniciar servidor FastAPI
python3 openssa_fastapi_server.py
