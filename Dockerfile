FROM python

WORKDIR /app


COPY . .

CMD ["python", "demo.py"]