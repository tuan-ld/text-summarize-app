# text-summarize-app

Using Django and Text Summarize Algorithm

This is the Heroku deployment of my app: https://text-summarize-app.herokuapp.com/

How to deploy:
1. Clone the app to the local
2. Set up Git  : https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) 
and Heroku CLI :https://devcenter.heroku.com/articles/heroku-cli#download-and-install
3. cd to the text-summarize-app folder you 've just cloned ```cd text-summarize-app```
4. Login to heroku : ```$heroku login```
5. Create your own heroku app: ```$heroku create YOUR_OWN_HEROKU_APP_NAME```
6. In cmd window type this code : ```$git init```
7. In cmd window type this code: ```$heroku git:remote -a herokudjangoapp```
8. In cmd window type this code : ```$git add .```
9. In cmd window type this code : ```$git commit -m "Initial commit"```
10. In cmd window type this code : ```$heroku config:set     DISABLE_COLLECTSTATIC=1```
10. In cmd window type this code : ```$git push heroku master```
11. Open app: ```$heroku open```
Done!
