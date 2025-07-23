# OpenSSA Server - Pantera Test 1

OpenSSA (Small Specialist Agents) server implementation for n8n integration.

## 🏗️ Arquitectura del Sistema
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   n8n EC2   │◄──►│ OpenSSA EC2 │◄──►│ AWS Services│
│ (existing)  │    │    (new)    │    │  S3/Lambda  │
└─────────────┘    └─────────────┘    └─────────────┘

## 📋 Detalles del Servidor

- **Instancia**: openssa-server (t3.large)
- **IP Pública**: 3.131.95.194
- **IP Privada**: 172.31.16.129
- **Versión OpenSSA**: 0.24.12.12
- **Python**: 3.12
- **OS**: Ubuntu 24.04 LTS

## ✅ Instalación Completada

- ✅ Instancia EC2 creada y configurada
- ✅ Entorno virtual Python configurado
- ✅ OpenSSA 0.24.12.12 instalado
- ✅ Arquitectura DANA probada
- ✅ Servidor FastAPI con auto-reload
- ✅ Integración con n8n funcionando

## 🔌 Endpoints de la API

### Health Check
```bash
GET http://3.131.95.194:8001/health
Consultar a OpenSSA
bashPOST http://3.131.95.194:8001/ask
Content-Type: application/json

{
  "question": "Tu pregunta aquí"
}
Documentación Automática

Swagger UI: http://3.131.95.194:8001/docs
ReDoc: http://3.131.95.194:8001/redoc

🛠️ Ambiente de Desarrollo
Configuración Inicial
bash# Clonar el repositorio
git clone https://github.com/jpaguirrech/openssa-pantera-server.git
cd openssa-pantera-server

# Copiar plantilla de configuración
cp environments/.env.development.example environments/.env.development

# Editar y agregar tu API key de OpenAI
nano environments/.env.development
Instalar Dependencias
bash# Crear entorno virtual
python3 -m venv openssa-env
source openssa-env/bin/activate

# Instalar dependencias
pip install -r requirements.txt
Iniciar Desarrollo
bash# Cargar ambiente y iniciar servidor FastAPI
./scripts/dev_start.sh
🔗 Integración con n8n
Para usar en n8n, configura el nodo HTTP Request:

URL: http://172.31.16.129:8001/ask (IP interna) o http://3.131.95.194:8001/ask (IP pública)
Método: POST
Headers: Content-Type: application/json
Body: {"question": "tu pregunta"}

📁 Estructura del Proyecto
pantera-test1-workspace/
├── environments/              # Configuraciones por ambiente
│   ├── .env.development.example  # Plantilla de configuración
│   └── .env.development          # Config local (no en Git)
├── scripts/                   # Scripts de automatización
│   ├── load_env.sh           # Cargar ambiente específico
│   └── dev_start.sh          # Iniciar servidor de desarrollo
├── logs/                     # Logs por ambiente
├── data/                     # Datos y archivos temporales
├── openssa_fastapi_server.py # Servidor FastAPI moderno
├── openssa_api_server.py     # Servidor original (puerto 8000)
├── dev_server.py             # Servidor de desarrollo (deprecated)
├── test_*.py                 # Scripts de prueba
├── requirements.txt          # Dependencias Python
└── README.md                 # Esta documentación
🧪 Pruebas
Probar Servidor Local
bash# Health check
curl http://3.131.95.194:8001/health

# Probar OpenSSA
curl -X POST http://3.131.95.194:8001/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "¿Qué es OpenSSA?"}'

# Probar desde n8n
# Usar HTTP Request node con URL: http://172.31.16.129:8001/ask
Comandos Útiles
bash# Cambiar ambiente
./scripts/load_env.sh [development|staging|production]

# Ver logs en tiempo real
tail -f logs/development.log

# Verificar puertos activos
ss -tlnp | grep -E ':(8000|8001)'

# Reiniciar servidor (auto-reload hace esto automáticamente)
./scripts/dev_start.sh
🚀 Tecnologías Utilizadas

OpenSSA: Framework de agentes neurosimbólicos
DANA: Arquitectura Domain-Aware Neurosymbolic Agent
FastAPI: Framework web moderno para APIs
Uvicorn: Servidor ASGI de alto rendimiento
Pydantic: Validación de datos y serialización
AWS EC2: Infraestructura de servidor
Python 3.12: Lenguaje de programación
Ubuntu 24.04: Sistema operativo

📝 Próximos Pasos

Configurar API keys de producción con AWS Secrets Manager
Crear agentes DANA especializados
Implementar procesamiento avanzado con OpenSSA
Configurar SSL/HTTPS para producción
Implementar logging y monitoreo avanzado
Escalar infraestructura según necesidad

🏷️ Tags
openssa ai n8n automation aws python dana api fastapi neurosymbolic agents
