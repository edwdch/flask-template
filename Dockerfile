FROM python:3.10
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

ARG DEFAULT_PORT=8080

COPY src src
EXPOSE ${DEFAULT_PORT}
HEALTHCHECK CMD curl -fs http://localhost:${DEFAULT_PORT}/api/ping || exit 1
# /app/logs is the log directory, which can be mounted when needed
VOLUME /app/logs
ENTRYPOINT ["python", "src/app.py"]