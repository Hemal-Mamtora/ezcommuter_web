import pyrebase

config = {
    "apiKey": "AIzaSyAESHEWWGGz_kmckJrLtGRoZ-vg015egLM",
    "authDomain": "ezcommuter.firebaseio.com",
    "databaseURL": "https://ezcommuter.firebaseio.com/",
    "storageBucket": "ezcommuter.appspot.com"
}

# initialize app with config
firebase = pyrebase.initialize_app(config)

# authenticate a user
auth = firebase.auth()
db = firebase.database()
