FROM python:3.11-slim

WORKDIR /app

# Copia apenas o requirements.txt que está dentro da pasta api
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copia só o conteúdo da pasta api para dentro do container
COPY ./api /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
