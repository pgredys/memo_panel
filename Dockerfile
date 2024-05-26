FROM python:3.8-alpine
LABEL authors="pgredys"

COPY . /memo_panel

WORKDIR /memo_panel

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["main.py" ]

EXPOSE 5000