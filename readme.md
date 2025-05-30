
<h1 align="center">Daily Fortune: AI-Powered Morning Motivation</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Deploy_with-WaveAssist-007F3B" alt="Deploy with WaveAssist" />
  <img src="https://img.shields.io/badge/Schedule-Daily%20at%2008%3A30-blue" alt="Daily Schedule" />
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License" />
  </a>
</p>

---

## 🚀 Overview

**Daily Fortune** is a simple, two-node workflow on [WaveAssist](https://waveassist.io) that delivers a random motivational or cautionary fortune to you every morning at 08:30. Use it to brighten your day, send yourself a friendly reminder, or integrate with email/SMS for automated delivery.


---

## 🔗 Pipeline Flow

```text
ChooseFortune → LogFortune
```

1. **ChooseFortune** (`choose_fortune.py`)

   * Initializes WaveAssist
   * Loads a predefined list of fortunes
   * Picks a random fortune
   * Stores the selected fortune under `today_fortune`
   * Prints it to the console

2. **LogFortune** (`log_fortune.py`)

   * Initializes WaveAssist
   * Fetches the stored `today_fortune`
   * Logs or displays the fortune
   * (Optional) Email or message the fortune to yourself

---

## 🧰 Features

* 🎲 **Random Fortune Selection**: A curated list of insights and reminders.
* ⏰ **Scheduled Execution**: Runs every day at 08:30 via WaveAssist’s scheduler.
* 💾 **Persistent Storage**: Keeps track of your daily fortune for future reference.
* 🔧 **Easy Customization**: Add or modify fortunes in `choose_fortune.py`, or extend the logging step to integrate with email, Slack, or SMS.

---

## 🎯 Getting Started

### One‑Click Deploy (Recommended)

<p align="center">
  <a href="https://waveassist.io/templates/daily-fortune-template" target="_blank">
    <img src="https://waveassistapps.s3.us-east-1.amazonaws.com/public/Button.png" alt="Deploy on WaveAssist" width="230" />
  </a>
</p>

1. Sign in or sign up at [WaveAssist](https://waveassist.io).
2. Navigate to **Templates → Daily Fortune**.
3. Click **Deploy** — WaveAssist imports the two nodes automatically.
4. Verify the schedule under **Nodes** and run once to test.
5. Enjoy your daily fortunes every morning at 08:30!

---

### 🏠 Local Setup

```bash
git clone https://github.com/WaveAssist/dailyfortune.git
cd dailyfortune
pip install waveassist
```

Set your API key:

```bash
export WAVEASSIST_API_KEY="your_api_key_here"
```

Initialize and schedule locally:

```bash
waveassist init
waveassist deploy --schedule
daily-fortune
```

*(Or run the scripts manually for testing:)*

```bash
python choose_fortune.py
python log_fortune.py
```

---

## ⚙️ Customization

* **Add Fortunes**: Edit the `fortunes` list in `choose_fortune.py`.
* **Change Schedule**: Adjust the `schedule` block in the YAML to run at different times or intervals.
* **Delivery Channels**: Extend `log_fortune.py` to send emails, push notifications, or Slack messages.

---

## 📖 Learn More

* WaveAssist docs: [waveassist.io/docs](https://waveassist.io/docs)
* Community: [waveassist.io/community](https://waveassist.io/community)
* Issues & feedback: [github.com/WaveAssist/dailyfortune/issues](https://github.com/WaveAssist/dailyfortune/issues)

---

Built with ❤️ by the WaveAssist team.
