FROM python:latest
WORKDIR /src/
COPY /src ./src
RUN pip install -r ./src/requirements.txt
#CMD ["python", "src/main.py"]