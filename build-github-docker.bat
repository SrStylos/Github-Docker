#!/bin/bash

echo "🚀 CONSTRUYENDO PROYECTO GITHUB-DOCKER"
echo "========================================"
echo "👤 Usuario: franchuu"
echo "📁 Directorio: Github-Docker"
echo "🏪 Proyecto: SrStylos Store"
echo ""

# Construir la imagen
docker build -f Dockerfile -t franchuu/github-docker-srstylos:latest .

echo ""
echo "✅ CONSTRUCCIÓN COMPLETADA"
echo "📦 Imagen: franchuu/github-docker-srstylos:latest"
echo "🐳 Ejecutar con: ./run-github-docker.bat"