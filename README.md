# recipe-app-api
Recipe api project with django, docker-compose, swagger, and TDD applied.

## ✨ command

1. build docker image
    > $ > docker-compose build
2. run docker container
    > $ > docker-compose up
3. test inspection
    > $ > docker-compose run --rm app sh -c "python manage.py test"
4. linting inspection
    > $ > docker-compose run --rm app sh -c "flake8"
5. Database run inspection
    > $ > docker-compose run --rm app sh -c "python manage.py wait_for_db"
7. docker volume list
     > $ > docker volume ls
