# Minimalistric tinyurl

## run a server

```
pip3 install -r requirements.txt
FLASK_ENV=development python3 server.py
```

## Storing a URL

```
curl -XPOST http://localhost:8088/api/v1/url/ --data url=https://localhost/

```

