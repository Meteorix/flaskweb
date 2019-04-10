#!/bin/sh

if [[ -d venv/bin ]];then
    echo "On Linux: start server 0.0.0.0:5000 with gunicorn"
    source venv/bin/activate
    gunicorn -b :5000 --access-logfile --error-logfile manage:app
else
    echo "On Windows: start server with gevent"
    source venv/Scripts/Activate
    python -u manage.py gvserver
fi
