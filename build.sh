set -o errexit # exit on error
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# create superuser
python manage.py create_superuser