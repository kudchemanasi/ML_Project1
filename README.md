# ML_Project1


### Software and account Requirement

1. GitHub account
2. Heroku Account
3. VS Code IDE
4. GIT cli

create python environment
```
python -m venv E:\ML_Project1\venv
```

```
pip install -r requirements.txt

```

To add files to git
```
git add . 
```
OR
```
git add <file_name>
```

Note : To ignore file or folder from git we write name of file/folder in .gitignore file

Check all version maintained by git 
```
git log
```

To commit the changes to git
```
git commit -m "Message"

```
To send changes to github
```
git push origin main

```

To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL 
2. HEROKU_API_KEY 
3. HEROKU_APP_NAME 

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```

NOTE: Image name for docker must be lowercase

To list docker image

```
docker image

```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 a033fb1695bc (Image ID)
```
To check the running cointainer in docker
```
docker ps

```

To stop docker container
```
docker stop <container_id>





