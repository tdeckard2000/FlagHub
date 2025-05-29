server:
	venv/bin/gunicorn server:app --bind 0.0.0.0:8000

dev:
	ENV=dev venv/bin/python3 server.py
