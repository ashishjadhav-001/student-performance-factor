#python image
FROM python:3.10.9-slim

#working directory
WORKDIR /student-app

# copy all the file in cantainer
COPY . /student-app

#install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Explose the port
EXPOSE 8000

#Run the fast api app
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]