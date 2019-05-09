# Basic User Administrator
Basic User Administration, managing CRUD and bank account data IBAN

## Instructions
Clone or download the project
```bash
git clone https://github.com/RafaPinzon93/basic_user_administration.git
```

### Configure using docker-compose
1. Download [Docker Desktop](https://www.docker.com/products/docker-desktop) for Mac or Windows. [Docker Compose](https://docs.docker.com/compose) will be automatically installed. On Linux, make sure you have the latest version of [Compose](https://docs.docker.com/compose/install/).
2. Run ```docker-compose up``` in this directory.
3. Stop docker container.
4. Run migrations ```docker-compose run web python manage.py migrate```
5. Start the server again ```docker-compose up```
6. The server will start running on http://localhost:8000

### Configure manually
Using python 3.7
1. Create a python virtual environment ```python -m venv virutal_env```
2. Activate the virtual environment
3. Install the requirements ```pip install -r requirements.txt```
4. Configure postgres database, and configure it in the settings file:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```
5. Run migrations ```python manage.py migrate```
6. Start the server ```python manage.py runserver```


## Using User Administrator
1. Go to http://localhost:8000, SignIn with your google Account.
2. This will redirect you to your users list page.
3. In the user list page, you can **create** your own users, **see** all the users created, and **update** or **delete** your own users.
4. When you **create** or **edit** an user, you can add the bank account data (**IBAN**). The system will validate the IBAN field checking the country code, the checksum digits and the Basic Bank Account Number.

### Trello for this Project
[User Administrator Trello](https://trello.com/b/TW3ZNnw0/user-administrator)