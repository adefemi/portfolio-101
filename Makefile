install:
	pip install -r requirements.txt

get_env:
	chmod +x ./getEnv.sh && ./getEnv.sh

load_env:
	python manage.py load_env.py

deploy:
	zappa deploy