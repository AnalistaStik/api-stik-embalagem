FROM python:3.10-slim

# Instala dependências essenciais
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

# Define diretório de trabalho
WORKDIR /app

# Copia projeto
COPY . .

# Instala dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]

