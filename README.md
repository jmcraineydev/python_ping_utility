# URL Tracker

### About the app

The URL Tracker is a simple application to track the status of URLs of apps you have deployed or want to monitor. This app makes a call every 20 minutes to all URLs registered and checks the return HTML response code logging/updating the URL status in the database. This app has a side effect of this periodic call, the URLs will remain active, and depending on your hosting service prevent your app from going to sleep on shared servers

### Technologies used in this app:

- Language used: Python 3.10 with Conda
- Framework: Flask
- Packages: werkzeug.security
- Database: MongoDB Atlas

### How to deploy:

1. You will need to set up a MongoDB Atlas cluster for this project. For your cluster, you will need the following:
   - user name
   - password
   - IP Address added to your cluster’s network security whitelist
   - the connection string for the cluster you are using for this project.
2. Fork this repo and clone it to your local machine
3. Setup .env file in your local environment containing the following information:

   - `APP_SECRET_KEY` <<A secret key (i.e. UUID) to config the instance of FLASK>>
   - `MONGO_DB_CONNECTION` <<the connection string you obtained from Mongo that should include your username and password in the string>>

4. Install the necessary packages: pymongo, werkzeug.security, etc

5. Running the APP:
   - In the terminal run `[main.py](http://main.py)` to start the server and load the flask frontend app
   - In a separate terminal run `[app.py](http://app.py)` to start begin checking URLs in the database every 20 minutes

### FEEDBACK/QUESTIONS:

If you have any feedback or questions on this app. Please create an issue in this Github repo.
