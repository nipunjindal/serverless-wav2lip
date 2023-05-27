FROM public.ecr.aws/docker/library/python:3.8.12-slim-buster

COPY requirements.txt  ./
RUN python -m pip install -r requirements.txt

COPY app.py  ./
COPY Wav2Lip/  Wav2Lip/
CMD ["python3", "app.py"]