FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements/requirements.txt
COPY . .
CMD [ "/bin/bash", "docker-entrypoint.sh" ]