# KandiDaten
a #makeopendata project
see http://make.opendata.ch/wiki/project:kandidaten

## Frontend

Install Node.js, npm, bower
Install Cairo (libcairo2-dev on Ubuntu, cairo-devel on Fedora Core)
Run a local web server (Nginx / Apache) or use `python -m SimpleHTTPServer`

## Backend

Install Python, ideally in a virtualenv, as well as pip, then
`pip install -r requirements.txt`

Run the API server with:
```
python api.py
```

Note: for the frontend and backend to talk they need to be on the same host
or Cross-Site-Scripting restrictions need to be temporarily disabled on your
browser. We are using this nginx configuration:
```
server {
    server_name kandidaten.local;
    root /opt/kandidaten/web/app/;
    location / {
        index index.html index.htm index.php;
    }
    location /api/ {
        proxy_pass http://localhost:5000;
    }
}
```

For more information see:

* `flask <https://github.com/mitsuhiko/flask>`_
* `peewee <https://github.com/coleifer/peewee>`_
* `wtforms <https://github.com/wtforms/wtforms>`_
* `wtf-peewee <https://github.com/coleifer/wtf-peewee>`_
