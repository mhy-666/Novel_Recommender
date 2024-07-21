# use an official Python runtime as a parent image
FROM python:3.9-slim

# set a directory for the app
WORKDIR /app

# copy current directory contents into the container at /app
COPY . /app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose the port 8501
EXPOSE 8501

# set the command to run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
