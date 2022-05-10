# docker-entrypoint.sh
#!/bin/bash
# Collect static files
# echo "Collect static files"
# python manage.py collectstatic --noinput
# Make migrations
echo "Make migrations"
python manage.py makemigrations
# Apply database migrations
echo "Apply database migrations"
python manage.py migrate
#Create Seeds
echo "Create Seeds"
python tools/seeds/make_data.py
exec "$@"