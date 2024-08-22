FROM python:latest
WORKDIR /src/
COPY src /src
COPY /main.py /
COPY /.env /
RUN pip install -r /src/requirements.txt
#CMD ["python", "src/main.py"]