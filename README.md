# Telegraph Cloud Uploader Bot


<p align="center">
    <b>A powerful Telegram bot to upload media to Catbox.moe.</b>
    <br>
    <a href="https://t.me/cantarellabots">
        <img src="https://img.shields.io/badge/Devs-CantarellaBots-blue?style=flat-square&logo=telegram" alt="Channel">
    </a>
</p>

---

## 🛠 Features
- ⚡ **Fast Uploads** (Catbox.moe)
- 🔗 **Permanent Links** (No Expiry)
- 🗂️ **User History** (`/history`)
- 📢 **Log Channel Support**
- 🛡️ **Admin Controls** (Ban, Broadcast)
- 🐳 **Docker & Heroku Support**

## 🚀 Deployment

### 💜 Heroku
<p>
<a href="https://heroku.com/deploy?template=https://github.com/cantarella-wuwa/imgtolink">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>

1. Fork this repo.
2. Create a new app on Heroku.
3. Connect GitHub repo.
4. Add Config Vars.
5. Deploy `worker` dyno.

### ☁️ Render (Free Tier Supported)
1. Fork this repo.
2. Create a new **Web Service** on Render.
3. Connect GitHub repo.
4. Add Environment Variables.
5. Deploy! (It runs on free tier).

### 🐳 Docker
```bash
docker build -t Cantarella-imgtolink .
docker run --env-file .env Cantarella-imgtolink
```

## ⚙️ Configuration
- `API_ID`: Get from my.telegram.org
- `API_HASH`: Get from my.telegram.org
- `BOT_TOKEN`: Get from @BotFather
- `MONGO_URL`: MongoDB Connection String
- `ADMINS`: User ID of Admin
- `LOG_CHANNEL`: Channel ID for logs (e.g., -100xxxx)

## 🤖 Bot Commands (for @BotFather)
Copy and paste this into BotFather:
```text
start - Start the bot
history - View your upload history
users - (Admin) Pannel
broadcast - (Admin) Broadcast message
ban - (Admin) Ban a user
unban - (Admin) Unban a user
```

## 👨‍💻 Credits
- **Developer**: [@cantarella_wuwa](https://t.me/cantarella_wuwa)
- **Channel**: [Cantarella Bots](https://t.me/cantarellabots)

<p align="center">
  <b>Don't copy without credit!</b>
</p>
