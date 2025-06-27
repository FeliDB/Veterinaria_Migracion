docker-compose down --volumes --remove-orphans 
docker-compose build
docker-compose up -d
sleep 6
docker-compose exec backend python manage.py makemigrations
sleep 6
docker-compose exec backend python manage.py migrate
sleep 6
python mongo_migrator/migrator.py