FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# RUN flask deploy
COPY . .
RUN flask deploy
CMD [ "/bin/bash", "docker-entrypoint.sh" ]