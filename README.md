# Chat_bot
A chatbot for Farmers

If you wish to deploy the chatbot on local machine first install all the dependencies
```
pip install -r requirements.txt
```
then simply run main.py
```
python3 main.py
```

# For deployment on heroku 
Clone this repository on local machine

Install heroku cli

log in to heroku through cli
```
heroku login -i
```
create a new heroku app.
```
heroku create
```
The `heroku create` CLI command creates a new empty application on Heroku, along with an associated empty Git repository. If you run this command from your app’s root directory, the empty Heroku Git repository is automatically set as a remote for your local repository.

To deploy your app to Heroku, you use the `git push` command to push the code from your local repository’s master or main branch to your heroku remote
```
git push heroku master
```
