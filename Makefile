run_default:
	python app.py

run_gunicorn:
	gunicorn -c gunicorn_config.py app:app
