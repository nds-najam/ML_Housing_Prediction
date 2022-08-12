# ML_Project_1
Application url:
[HousingPredictor](https://ml-regression-app.herokuapp.com/)

## Start Machine Learning project.

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment
```
conda create -p venv python==3.7 -y
conda activate venv/ or conda activate venv
```
Install all libraries
```
pip install -r requirements.txt
```
Git commands
```
git add . (all files)
git add <filename> (for adding one file)
git status (to check current status)
git log (to see all the logs)
git commit -m "message" (Commiting the changes)
git push origin main (Send changes to github)
git remote -v (To check remote url)
git branch (to check current branch)
```
Git commands available at
```
https://git-scm.com/docs/git
```
To setup CI/CD pipeline in heroku we need 3 points of information

1. HEROKU_EMAIL = <>
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = <>

Docker Commands
```
docker build -t <image_name>:<tagname> . # (Builds Docker Image, image name for docker should be lowercase)
docker images # (To list docker image)
docker run -p 5000:5000 -e PORT=5000 f8c749e73678 # (run docker image)
docker ps # to check running container in docker
docker stop <container_id> # to stop docker container
```
Git actions available at https://docs.github.com/en/actions

