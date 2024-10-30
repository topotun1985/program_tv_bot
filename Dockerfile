# Отдельный "сборочный" образ
FROM python:3.11-slim-bullseye as compile-image
RUN python -m venv venv
ENV PATH="venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt



# Образ, который будет непосредственно превращаться в контейнер
FROM python:3.11-slim-bullseye as run-image
COPY --from=compile-image venv venv
ENV PATH="venv/bin:$PATH"
WORKDIR /program_tv_bot
COPY . main
CMD ["python", "-m", "main"]