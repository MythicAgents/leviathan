FROM python:3.11-alpine AS builder

COPY [".docker/requirements.txt", "requirements.txt"]

RUN apk add gcc build-base linux-headers git
RUN git clone https://github.com/pawliczka/CRX3-Creator /CRX3-Creator
RUN python3 -m pip wheel --wheel-dir /wheels -r requirements.txt

FROM python:3.11-alpine

COPY --from=builder /wheels /wheels
COPY --from=builder /CRX3-Creator /CRX3-Creator

RUN pip install --no-cache /wheels/*

WORKDIR /Mythic/
COPY [".", "."]
CMD ["python3", "main.py"]