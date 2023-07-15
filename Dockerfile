FROM python
WORKDIR /app
COPY . /app/
RUN pip install pandas
RUN pip install pyodbc 

ENTRYPOINT ["python3", "pipeline.py"]