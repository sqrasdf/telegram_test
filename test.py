import telegram
import asyncio
import os 
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TOKEN")
sqr_id = os.environ.get("sqr_id")
group_id = os.environ.get("group_id")

bot = telegram.Bot(token=TOKEN)

async def main():
    task_video = asyncio.create_task(bot.send_video(chat_id=sqr_id, video="https://c.tenor.com/k2Ub9GzzyCYAAAAM/jp2gmd-polishpope.gif"))
    task_message = asyncio.create_task( bot.send_message(chat_id=sqr_id, text="nice"))

    res_video = await task_video
    res_message = await task_message


asyncio.run(main())
