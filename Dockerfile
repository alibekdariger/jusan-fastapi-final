FROM python:3.8

RUN pip install fastapi uvicorn

EXPOSE 8080

COPY main.py /

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
