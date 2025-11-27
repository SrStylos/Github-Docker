#!/bin/bash

echo "🛑 DETENIENDO PROYECTO GITHUB-DOCKER"
echo "====================================="

# Detener y eliminar contenedores
docker-compose -f docker-compose-github-docker.yml down

echo ""
echo "✅ APLICACIÓN DETENIDA"
echo "📁 Directorio: Github-Docker"
echo "👤 Usuario: franchuu"