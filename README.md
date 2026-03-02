🛡️ TRACEBROWSE – Browser-Based User Behavior Analytics (UBA)

TRACEBROWSE is a browser-centric User Behavior Analytics (UBA) and forensic monitoring platform designed to provide real-time visibility into internal browsing activity.
It helps security teams and researchers detect risky behavior, login attempts, and build accurate forensic timelines for SOC, VAPT, and insider-threat use cases.

🎯 Project Objective

The primary goal of TRACEBROWSE is to:

Monitor live browser activity

Detect security-relevant behavior

Provide a clear forensic timeline

Demonstrate how lightweight browser instrumentation can support SOC and security investigations

This project is built strictly for educational, research, and authorized internal monitoring purposes.

🚀 Key Features

Real-Time Browser Activity Monitoring
Captures live page titles and full URLs from active browser tabs.

Login Page & Sensitive Activity Detection
Automatically identifies login pages and security-related browsing patterns.

Behavior Classification & Risk Levels
Events are categorized into:

NORMAL

LOGIN

WARNING

Live SOC-Style Dashboard
Dark-mode, analyst-friendly dashboard with automatic refresh and real-time statistics.

Forensic URL Tracking
Full URL capture enables reconstruction of browsing paths during investigations.

Noise Filtering
Internal dashboard traffic and irrelevant system URLs are automatically excluded.

Smart Filtering (UI)
Quickly filter events such as login pages, media activity, or security-related searches.

🛠️ Tech Stack

Backend

Python

Flask

Frontend

HTML5

CSS3 (Dark UI / Inter font)

JavaScript (AJAX polling)

Browser Instrumentation

Custom Chrome Extension

Background Service Worker

Tab activation & update listeners

Data Handling

JSON-based communication

Optional CSV logging for forensic review

📦 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/YourUsername/TRACEBROWSE.git
cd TRACEBROWSE
2️⃣ Install Python Dependencies
pip install -r requirements.txt
3️⃣ Run the Backend Server
python main.py

The dashboard will be available at:

http://127.0.0.1:5000
4️⃣ Load the Chrome Extension

Open Chrome and navigate to:

chrome://extensions/

Enable Developer Mode

Click Load unpacked

Select the uba_chrome_extension folder

Once loaded, browser activity will start appearing on the dashboard in real time.

📊 Dashboard Overview

The dashboard provides:

A live event timeline

Clear visibility into browsing behavior

Highlighted login-related and security-sensitive activity

A clean SOC-style monitoring experience

🔐 Security & Privacy Notes

TRACEBROWSE does NOT capture:

Passwords

Keystrokes

Form inputs

Personal data

Only metadata (page title, URL, timestamp) is collected.

Intended for authorized environments only.

📜 License

This project is licensed under the MIT License.
See the LICENSE file for details.

👨‍💻 Author

Varun Rajput 🇮🇳
Cybersecurity | VAPT | Security Tool Development

🖼️ Screenshots


(Add dashboard and live monitoring screenshots here)

✅ FINAL NOTE

This project demonstrates:

Practical understanding of User Behavior Analytics

Real-time monitoring concepts used in SOC environments

Secure and ethical browser-based instrumentation
