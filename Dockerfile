# Imagen base para proyecto Github-Docker de franchuu
FROM python:3.11-alpine

# Metadatos personalizados para franchuu
LABEL maintainer="franchuu"
LABEL version="2.0"
LABEL description="SrStylos Store - Proyecto Github-Docker de franchuu"
LABEL project="Github-Docker"

# Directorio de trabajo dentro del container
WORKDIR /app-github-docker

# Copiar archivo de dependencias
COPY requirements-franchuu.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements-franchuu.txt

# Copiar aplicación principal
COPY app-franchuu.py .

# Exponer puerto
EXPOSE 8080

# Health check personalizado
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8080/ || exit 1

# Comando de inicio
CMD ["python", "app-franchuu.py"]