FROM python:3.11-slim

# RUN apt-get update && apt-get install -y gcc libpq-dev \
#     && pip install --no-cache-dir -r requirements.txt \
#     && apt-get purge -y --auto-remove gcc libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p profiles
RUN chmod 777 profiles

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
