# use an official Python runtime as a parent image
FROM python:3.9-slim


# set a directory for the app
WORKDIR /Novel_Recommender

# copy current directory contents into the container at /app
COPY . /Novel_Recommender

# install dependencies
RUN pip3 install -r requirements.txt

# expose the port 8501
EXPOSE 8501

# set the command to run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# set env var
ENV LLAMAFILE_URL="http://127.0.0.1:8080/v1"
