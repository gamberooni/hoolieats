FROM python:3.8.14-slim
WORKDIR /app
COPY requirements-extra.txt .
RUN apt-get update \
    # && apt-get -y --no-install-recommends install build-essential curl \
    && pip install --no-cache-dir poetry==1.2.1 \
    && poetry install \
    && pip install -r requirements-extra.txt \
    # && apt-get remove -y build-essential \
    && apt-get clean \
    && rm -rf /var/cache/apt/lists 
COPY hoolieats hoolieats
COPY hoolieats-dbt hoolieats-dbt

EXPOSE 8501
ENTRYPOINT [ "streamlit", "run" ]
CMD [ "app.py" ]
