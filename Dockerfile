FROM python:3.10-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

# Define diretório de trabalho
WORKDIR /app

# Copia o código da API
COPY . .

# Instala dependências Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Porta usada em produção
EXPOSE 5000

# Comando de inicialização
CMD ["python", "app.py"]

