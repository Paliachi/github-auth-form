# AUTH GITHUB TEST PROJECT

## Set up the project

### Clone the project from GitHub:
```shell
git clone https://github.com/Paliachi/github-auth-form.git
```
### Create and update .env file based on .env.example.
### Run docker compose:
```
docker-compose up
```

#### Note: Docker compose runs services - web and db.

### Open your browser and go to [localhost:8000/login/](http://localhost:800/login)

#### Note: Check Makefile for some fast commands.
```
make help    
```

## FLOW
### User can be logged only from GitHub: [LOGIN URL](http://localhost:800/login). The profile is automatically created for User.
### After login User is redirected to a profile: [PROFILE URL](http://localhost:800/profile). Appears data of User.
### Profile data can be updated: [PROFILE UPDATE URL](http://localhost:800/profile-form)

