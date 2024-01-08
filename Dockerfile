FROM python:3.8.18

WORKDIR /app
ADD . /app

RUN apt-get update && apt-get install -y libgomp1
RUN pip install -r requirements.txt

EXPOSE 1664

CMD streamlit run --server.port 1664 streamlit_docker.py
