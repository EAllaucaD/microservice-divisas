# Usa una imagen base oficial de Python 3 en Alpine Linux
FROM python:3.9-alpine

# Instala las dependencias necesarias
RUN apk update && apk add --no-cache \
    python3-dev \
    py3-pip \
    build-base

# Actualiza pip a la última versión disponible
RUN pip install --upgrade pip

# Instala Flask, requests y dotenv
RUN pip install Flask requests python-dotenv



# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . .

# Comando por defecto para ejecutar la aplicación
CMD ["python", "divisas.py"]
