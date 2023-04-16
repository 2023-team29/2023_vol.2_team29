FROM python:3.11
ENV PYTHONBURRERED=1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip install openai
ENV API_KEY=${API_KEY}
RUN pip install python-dotenv