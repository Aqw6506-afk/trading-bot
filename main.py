import time
import random

def get_signal():
    signals = ["LONG", "SHORT", "WAIT"]
    return random.choice(signals)

def run_bot():
    print("交易機器人啟動中...")
    while True:
        signal = get_signal()
        print(f"當前訊號: {signal}")

        if signal == "LONG":
            print("做多進場")
        elif signal == "SHORT":
            print("做空進場")
        else:
            print("觀望中")

        time.sleep(10)

if __name__ == "__main__":
    run_bot()
