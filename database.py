import motor.motor_asyncio
from config import Config

class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id):
        return dict(
            id=id,
            banned=False
        )

    async def add_user(self, id):
        user = await self.col.find_one({'id': int(id)})
        if not user:
            user = self.new_user(id)
            await self.col.insert_one(user)
            return True
        return False

    async def is_banned(self, id):
        user = await self.col.find_one({'id': int(id)})
        return True if user and user.get('banned') else False
    
    async def ban_user(self, id):
        await self.col.update_one({'id': int(id)}, {'$set': {'banned': True}})
        
    async def unban_user(self, id):
        await self.col.update_one({'id': int(id)}, {'$set': {'banned': False}})

    async def add_upload(self, user_id, link):
        # Push to history array, keep only last 10
        await self.col.update_one(
            {'id': int(user_id)},
            {'$push': {'history': {'$each': [{'link': link, 'date': None}], '$slice': -10}}}
        )

    async def get_history(self, user_id):
        user = await self.col.find_one({'id': int(user_id)})
        return user.get('history', []) if user else []

    async def get_all_users(self):
        return self.col.find({})

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

db = Database(Config.MONGO_URL, "Cantarellabots-imgtolinkBot") if Config.MONGO_URL else None
