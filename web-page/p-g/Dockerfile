# Use uma imagem base Python
FROM python:3.9

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie os arquivos necessários para o contêiner
COPY requirements.txt .
COPY app.py .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta em que o aplicativo Flask está sendo executado
EXPOSE 5000

# Defina a variável de ambiente para o Flask
ENV FLASK_APP=app.py

# Inicie o aplicativo Flask
CMD [ "flask", "run", "--host=0.0.0.0" ]
