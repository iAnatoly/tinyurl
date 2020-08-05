# Minimalistric tinyurl

## Run as a local HTTP server

```
pip3 install -r requirements.txt
FLASK_ENV=development python3 server.py
```

This will run teh server on :8088. Update server.py to change the port.

## Storing a URL

```
curl -XPOST http://localhost:8088/api/v1/url/ --data url=https://localhost/

```

## Listing all URLs in the datastore
This method exists just for debug purpose, and requires (mock) authorization

```
curl http://localhost:8088/api/v1/url/ -H 'Authorization: Bearer bear'

```


