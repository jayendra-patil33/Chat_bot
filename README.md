# Chat_bot
A chatbot meant for Farmers
# init a local git repository
# all the development should be done and tested locally first 
# Once the first version of application is ready, push it to githu repository
# Install heroku cli 
cd [PATH]
git init
git add * 
git commit -m "type message here"
git push
# init the pip requirements.file
git add *
pip install -r requirements.txt
# once all the packages have been install you can freeze the requirements.file
# make sure the name of the file is only "requirements.txt
git commit -m "type message here"
git push
# log in to heroku through cli
heroku login -i
# create a new heroku app
heroku create
# make a procfile to write the command to be executed by the dyno
# push the change to the remote git repository where the heroku app is stored
git push heroku master

