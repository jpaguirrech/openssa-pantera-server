#!/bin/bash

# Script para cargar ambiente específico
ENVIRONMENT=${1:-development}
ENV_FILE="/home/ubuntu/pantera-test1-workspace/environments/.env.$ENVIRONMENT"

if [ ! -f "$ENV_FILE" ]; then
    echo "❌ Error: Archivo no encontrado: $ENV_FILE"
    exit 1
fi

echo "🔄 Cargando ambiente: $ENVIRONMENT"

# Cargar variables de entorno
set -a
source "$ENV_FILE"
set +a

echo "✅ Ambiente $ENVIRONMENT cargado"
echo "   - HOST: $OPENSSA_HOST:$OPENSSA_PORT"
echo "   - LOG_LEVEL: $LOG_LEVEL"
echo "   - DEBUG: $DEBUG"

# Crear directorios necesarios
mkdir -p $(dirname "$LOG_FILE_PATH")
mkdir -p /home/ubuntu/pantera-test1-workspace/data/temp

echo "📁 Directorios verificados"
