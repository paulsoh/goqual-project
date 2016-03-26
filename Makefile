clean:
		find . -name "*.pyc" -exec rm -rf {} \;
		find . -name "*.swp" -exec rm -rf {} \;


migrate:
		python goqual/manage.py makemigrations goqual video
		python goqual/manage.py migrate


test:
		python goqual/manage.py test
