# Imagen base de Python
FROM python:3.11

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Exponer el puerto del servidor
EXPOSE 8000

# Comando para correr el backend
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
