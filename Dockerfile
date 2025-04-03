FROM python
RUN mkdir -p /opt/app && pip install Django
WORKDIR /opt/app
COPY . /opt/app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]