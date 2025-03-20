from python:3.10


workdir /app

copy requirements.txt requirements.txt

run pip3 install --upgrade setuptools
run pip3 install -r requirements.txt
run chmod 755 .

copy . .

CMD ["sh", "-c", "python test.py"]
