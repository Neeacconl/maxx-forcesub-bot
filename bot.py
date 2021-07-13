from pyrogram import Client
from Config import Config


plugins = dict(
    root="plugins",
    include=[
        "start",
        "help",
        "forceSubscribe"
    ]
)

app = Client(
     'eagle_eye',
      bot_token = 1841388817:AAHDhHC3hK0GYnIdszzHceV9meYiPOkAcmA,
      api_id = 2744894,
      api_hash = f033339c953e40d8366017033712c530,
      plugins = plugins
)

app.run()
