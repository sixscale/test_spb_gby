
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD celery -A test_spb_gby worker -l info & daphne test_spb_gby.asgi:application
