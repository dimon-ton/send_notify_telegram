import json
import requests
from dotenv import load_dotenv
import os




def send_telegram_notify():
   load_dotenv()
   token = os.getenv("TELEGRAM_TOKEN")  # Telegram bot token ของเรา
   chat_id = os.getenv("USER_ID")  # Chat ID ของเรา
   
   message = "Hello Telegram Group from python"  # ข้อความที่จะส่ง


   telegram_url = f"https://api.telegram.org/bot{token}/sendMessage" # URL สำหรับส่งข้อความ


   payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"} # Telegram payload ที่จะส่งไป ประกอบด้วย chat_id, text และ parse_mode (ในที่นี้เราใช้ Markdown)


   headers = {"Content-Type": "application/json"} # ส่วน header ของ request ที่เราส่งไป ในที่นี้เราใช้ Content-Type เป็น application/json เนื่องจากเราส่งข้อมูลเป็น JSON
   response = requests.post(telegram_url, headers=headers, data=json.dumps(payload))


   # ตรวจสอบว่าส่งข้อความสำเร็จหรือไม่
   if response.status_code == 200:
       print("ส่งข้อความสำเร็จ!")
   else:
       print(f"ส่งไม่สำเร็จ: {response.text}")




# Call the function
send_telegram_notify()
