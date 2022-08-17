FROM python

USER 0

COPY ./developers_code/app1.py /app/

RUN pip install flask

CMD ["python3", "/app/app1.py"]
