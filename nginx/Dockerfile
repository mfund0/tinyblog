FROM nginx:latest
RUN apt-get update -y
RUN apt-get install -y python-pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY boot.sh ./
RUN chmod +x ./boot.sh

COPY nginx.j2 ./
ENTRYPOINT ["./boot.sh"]
