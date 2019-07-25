FROM python:3.6-slim
COPY . /app
WORKDIR /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["python", "app.py"]
