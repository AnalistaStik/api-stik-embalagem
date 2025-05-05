FROM python:3.10-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    gnupg \
    curl \
    unixodbc-dev \
    unixodbc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala o driver ODBC da Microsoft
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Define diretório da app
WORKDIR /app

# Copia tudo para dentro do container
COPY . .

# Instala dependências Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
