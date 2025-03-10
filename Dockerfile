from python

workdir /usr/src/app

copy requirements.txt ./
run pip install --no-cache-dir -r requirements.txt

copy . .
cmd ["/bin/bash", "-c", "python3 app.py"]

        
