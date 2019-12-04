COPY requirements-simple.txt /
RUN pip install -r /requirements-simple.txt



EXPOSE 8050
CMD ["python", "./app.py"]