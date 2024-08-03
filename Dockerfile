FROM python:3.11

WORKDIR /SD_to_HD_Video_ESRGAN

COPY . /SD_to_HD_Video_ESRGAN

WORKDIR /SD_to_HD_Video_ESRGAN

RUN pip install -r requirements.txt

EXPOSE $PORT

CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:$PORT", "app:app"]
