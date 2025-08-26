FROM python:3.11-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# Install dependencies
COPY ./requirements.txt /code/
RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . /code/

EXPOSE 8000

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
