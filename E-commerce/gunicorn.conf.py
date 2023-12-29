# gunicorn.conf.py

bind = "0.0.0.0:8000"  # Bind to all network interfaces on port 8000
workers = 4  # Number of worker processes
worker_class = "gevent"  # Use the Gevent worker class
import sys

print(sys.path)
