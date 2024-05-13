FROM python:3.10
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
ENV PORT 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
