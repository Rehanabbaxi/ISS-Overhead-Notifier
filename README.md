# 📡 ISS Overhead Notifier

This project checks if the **International Space Station (ISS)** is currently passing over your location **at night**,  
and if so, it sends you an **email notification** to look up at the sky! ✨🚀

---

## ✨ Features
- ✅ Fetches the ISS’s live location using [Open Notify API](http://api.open-notify.org/iss-now.json)
- ✅ Checks if the ISS is within ±5° latitude/longitude of your location
- ✅ Uses [Sunrise–Sunset API](https://sunrise-sunset.org/api) to determine if it’s dark
- ✅ Sends an email notification when conditions are met

---

## 🛠️ How It Works
1. Every 60 seconds, the script:
   - Gets your current time and checks if it’s night.
   - Gets the ISS’s current position.
   - Checks if the ISS is near your location (within ±5° latitude/longitude).
2. If both conditions are true, it sends an email:
