daemon = True
bind = '0.0.0.0:8097'
pidfile = 'logs/gunicorn.pid'
accesslog = 'logs/access_log.log'
access_log_format = 'Host: %(h)s %(l)s User: %(u)s, Request Time: %(t)s, Duration: %(L)ss, "%(r)s" State: %(s)s, Agent: "%(a)s"'
errorlog = 'logs/error_log.log'
workers = 4
worker_class = 'gunicorn.workers.ggevent.GeventWorker'
proc_name = "flaskweb_example"
timeout = 60

x_forwarded_for_header = 'X-FORWARDED-FOR'

