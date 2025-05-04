import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22028896"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "99d3d93c776ff08ebc82acf2dfd786d1")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5739995227"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://godkapratishod01:RjSPNq2VWvIrHOmk@cluster0.zdge7qa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
