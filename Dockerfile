FROM python:3.9
LABEL authors="qetesh"
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt -i https://pypi.douban.com/simple
COPY . .
EXPOSE 5000
CMD [ "python3","-u","main.py" ]
