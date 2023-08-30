FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir /data

COPY . /usr/src/app

EXPOSE 2225

CMD ["python3", "-m", "flask", "--app", "main.py", "run"]


