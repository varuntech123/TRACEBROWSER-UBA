# 🛡️ TRACEBROWSE
### **Browser-Based User Behavior Analytics (UBA) & Forensic Engine**

TRACEBROWSE is a professional-grade User Behavior Analytics (UBA) and forensic monitoring platform designed to provide real-time visibility into internal browsing activity. It helps security teams and researchers detect risky behavior, identify unauthorized login attempts, and build accurate forensic timelines for SOC, VAPT, and insider-threat investigations.



---

## 🎯 Project Objective
The primary goal of **TRACEBROWSE** is to demonstrate how lightweight browser instrumentation can support enterprise security:
- **Monitor** live browser activity across multiple tabs.
- **Detect** security-relevant behavior and sensitive page access.
- **Provide** a structured forensic timeline for incident response.
- **Ethics-First:** Built strictly for authorized internal monitoring and educational research.

## 🚀 Key Features

- **Real-Time Activity Stream:** Captures live page titles and full URLs with 0% latency.
- **Intelligence-Driven Classification:** Automatically categorizes events into:
    - 🟢 **NORMAL:** Routine business browsing.
    - 🟡 **WARNING:** Access to VAPT tools or vulnerable platforms.
    - 🔴 **LOGIN:** Detection of authentication portals and sensitive gateways.
- **SOC-Style Dashboard:** Analyst-friendly Dark UI featuring real-time statistics and AJAX polling.
- **Forensic URL Tracking:** Full reconstruction of a user’s browsing path during a security audit.
- **Noise Filtering:** Automatically excludes internal dashboard traffic to keep logs clean and actionable.
- **Smart UI Filters:** Sidebar logic to isolate Login pages, Media activity, or Security searches.



## 🏗️ Tech Stack

### **Backend**
- **Python (Flask):** Robust REST API for data ingestion and dashboard serving.
- **Flask-CORS:** Secure cross-origin communication between browser and server.

### **Frontend**
- **HTML5/CSS3:** Modern "Inter" font integration with a high-contrast Dark UI.
- **JavaScript (jQuery/AJAX):** Asynchronous polling for real-time dashboard updates without page refresh.

### **Browser Instrumentation**
- **Custom Chrome Extension:** - **Background Service Worker:** Continuous monitoring of tab states.
    - **Extension API:** Utilizing `chrome.tabs` listeners for precise metadata capture.

---

📸 Dashboard Overview
The TRACEBROWSE dashboard acts as a centralized Security Operations Center (SOC) view, highlighting high-risk behavior in real-time.

🔐 Security & Privacy Notes
Metadata Only: TRACEBROWSE focuses on forensics. It does NOT capture passwords, keystrokes, form inputs, or personal private data.

Compliance: Intended for use in authorized corporate environments or local research labs only.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

Developed with 🛡️ by Varun Rajput Cybersecurity | VAPT | Security Tool Development 🇮🇳 Bhopal, India




## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone [https://github.com/YourUsername/TRACEBROWSE.git](https://github.com/YourUsername/TRACEBROWSE.git)
cd TRACEBROWSE


2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Engine
python main.py

Dashboard Access: Open http://127.0.0.1:5000 in your preferred browser.

4️⃣ Load the Extension
1 = Open Chrome and navigate to chrome://extensions/.
2 = Enable Developer Mode (top right).
3 = Click Load Unpacked and select the uba_chrome_extension folder.

<img width="1852" height="973" alt="s1" src="https://github.com/user-attachments/assets/f00a1d48-0ecb-4519-9c1a-7f61983c2d2b" />
<img width="1868" height="645" alt="s2" src="https://github.com/user-attachments/assets/71d6c725-a3b2-4808-9559-94a4f321fd97" />
<img width="1878" height="747" alt="s3" src="https://github.com/user-attachments/assets/e8518ebc-2b02-45fa-8607-154b436b5f4b" />
<img width="1877" height="613" alt="s4" src="https://github.com/user-attachments/assets/f7c08953-2fdf-43d8-9e0e-bcf9a7402e83" />
<img width="1865" height="567" alt="s5" src="https://github.com/user-attachments/assets/112be816-6711-4ce9-96a9-4f24817a5886" />
