#คำนวณแนวโน้มหุ้น
import yfinance as yf
import pandas as pd
from ta.trend import EMAIndicator 
from ta.momentum import RSIIndicator 

# เลือกหุ้นที่ต้องการทราบแนวโน้ม
ticker = (input ("ระบุชื่อหุ้น..."))

#ดึงข้อมูลราคา
df = yf.download(ticker, period="6mo", interval="1d")
df.columns = df.columns.get_level_values(0)

if df.empty:
    print("ไม่พบข้อมูลหุ้น")
    exit()

close = df["Close"].squeeze()

#คำนวณ ema50
ema50 = EMAIndicator(close=close, window=50)
df["EMA50"] = ema50.ema_indicator()

#คำนวณ RSI
rsi = RSIIndicator(close=close, window=14)
df["RSI"] = rsi.rsi()

#ข้อมูลล่าสุด
latest_close = df["Close"].iloc[-1]
latest_ema50 = df["EMA50"].iloc[-1]
latest_rsi = df["RSI"].iloc[-1]

score = 0

#เงื่อนไข
if latest_close > latest_ema50:
    score += 50
    ema_signal = "Bullish"
else:
    ema_signal = "Bearish"

if 50 < latest_rsi < 70:
    score += 50
    rsi_signal = "Momentum ขาขึ้น"
elif latest_rsi >= 70:
    rsi_signal = "Overbought"
elif latest_rsi <= 30:
    rsi_signal = "Oversold"
else:
    rsi_signal = "Neutral"

    
    print("-" * 30)
    print(f"หุ้น: {ticker}")
    print(f"ราคาปิด: {latest_close:.2f}")
    print(f"RSI: {latest_rsi:.2f}")
    print(f"EMA Signal: {ema_signal}")
    print(f"RSI Signal: {rsi_signal}")
    print(f"Score: {score}/100")

    if score >= 70:
        print("แนวโน้ม: มีโอกาสขึ้น")
    elif score >= 40:
        print("แนวโน้ม: Sideway")
    else:
        print("แนวโน้ม: มีโอกาสลง")