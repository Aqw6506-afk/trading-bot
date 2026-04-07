from flask import Flask
import threading
import time

app = Flask(__name__)

def run_bot():
    while True:
        print("bot running...")
        
        # ✅ 這裡放你的交易程式
        # 例如：
        # trade()
        
        time.sleep(10)

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=10000)
