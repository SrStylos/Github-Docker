#!/bin/bash

echo "🏪 INICIANDO SrStylos Store - Github-Docker"
echo "============================================"
echo "👤 Propietario: franchuu"
echo "📁 Directorio: Github-Docker"
echo "🌐 Puerto: 8080"
echo ""

# Ejecutar con Docker Compose
docker-compose -f docker-compose-github-docker.yml up -d

echo ""
echo "✅ APLICACIÓN INICIADA"
echo "📍 URL: http://localhost:8080"
echo "📊 Ver logs: docker logs github-docker-franchuu"
echo "🛑 Detener: ./stop-github-docker.sh"