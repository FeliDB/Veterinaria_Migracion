docker-compose down --volumes --remove-orphans 
docker-compose build
docker-compose up -d
wait 6
docker-compose exec backend python manage.py makemigrations
wait 6
docker-compose exec backend python manage.py migrate
wait 
python mongo_migrator/migrator.py