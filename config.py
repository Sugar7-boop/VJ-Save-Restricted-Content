import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20763817"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "07186e8f2ffe607e99eedf7eaa5e630b")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://dasaripardhasaradhi141:X5SstfxEbJORxOTh@cluster0.fvgzzwq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
