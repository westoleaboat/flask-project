FROM python:3.10
WORKDIR /app
COPY /requirements/common.txt .
RUN pip install --no-cache-dir --upgrade -r requirements/common.txt
COPY . .
CMD [ "/bin/bash", "docker-entrypoint.sh" ]