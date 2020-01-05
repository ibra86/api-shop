FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN ls -lsaF

EXPOSE 5000

WORKDIR src

CMD python app.py