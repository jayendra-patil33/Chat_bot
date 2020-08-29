# Chat_bot
A chatbot for Farmers

If you wish to deploy the chatbot on local machine 
First install all the dependencies
```
pip install -r requirements.txt
```
then simply run main.py
```
python3 main.py
```

# For deployment on heroku 
Install heroku cli

cd [PATH]
git init
git add * 
git commit -m "type message here"
git push
init the pip requirements.file
git add *
pip install -r requirements.txt
once all the packages have been install you can freeze the requirements.file
make sure the name of the file is only "requirements.txt
git commit -m "type message here"
git push
log in to heroku through cli
heroku login -i
create a new heroku app
heroku create
make a procfile to write the command to be executed by the dyno
push the change to the remote git repository where the heroku app is stored
git push heroku master

