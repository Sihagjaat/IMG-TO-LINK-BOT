# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat

from pyrogram import Client, idle
from config import Config
from web_server import web_server
from aiohttp import web
import os
import asyncio

# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
app = Client(
    "Cantarellabots-imgtolinkbot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
if __name__ == "__main__":
    print(r"""
   ______            __                  __  __        ____        __       
  / ____/___ _____  / /_____ _________  / / / /___ _  / __ )____  / /______ 
 / /   / __ `/ __ \/ __/ __ `/ ___/ _ \/ / / / __ `/ / __  / __ \/ __/ ___/ 
/ /___/ /_/ / / / / /_/ /_/ / /  /  __/ / / / /_/ / / /_/ / /_/ / /_(__  )  
\____/\__,_/_/ /_/\__/\__,_/_/   \___/_/_/_/\__,_/ /_____/\____/\__/____/   
                                                                            
      BOT WORKING PROPERLY....
    """)
    print("Starting Bot...")
    
    # Start Web Server for Render/Heroku
    port = int(os.environ.get("PORT", 8080))
    
    # We need to run standard asyncio loop for both
    loop = asyncio.get_event_loop()
    
    try:
        app.start()
        print("Bot Started! Send /start to verify.")
        
        # Web Server Startup
        web_app = loop.run_until_complete(web_server())
        runner = web.AppRunner(web_app)
        loop.run_until_complete(runner.setup())
        site = web.TCPSite(runner, "0.0.0.0", port)
        loop.run_until_complete(site.start())
        print(f"Web Server started on port {port}")
        
        idle()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        app.stop()
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
