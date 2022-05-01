FROM python:3.9.5-slim
WORKDIR /app
COPY requirements.txt .
RUN apt-get update \
    && apt-get -y --no-install-recommends install build-essential libpq-dev curl \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y build-essential libpq-dev \
    && apt-get clean \
    && rm -rf /var/cache/apt/lists 
COPY src .
COPY RCdata RCdata
EXPOSE 8501
ENTRYPOINT [ "streamlit", "run" ]
CMD [ "./app.py" ]
