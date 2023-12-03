FROM python
WORKDIR /file_management
COPY . /file_management
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]