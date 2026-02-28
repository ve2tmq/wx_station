# 📻 OpenWX-Canada: The Volunteer-Driven Weather Radio Relay

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Proof_of_Concept-orange)

## 🌪️ The Project (The "Why")
On March 16, 2026, Environment Canada will cease broadcasting weather forecasts on dedicated VHF channels (the WX band). Millions of emergency weather radios, marine VHFs, and scanners across the country will go silent. 

**OpenWX-Canada** is an open-source initiative aimed at replacing this government infrastructure with a resilient citizen network, managed by and for the amateur radio community. This Python script allows any club or enthusiast to turn a simple computer (or a Raspberry Pi) and a surplus commercial VHF transmitter into a fully automated, continuous weather broadcasting station.

Our goal is simple: Keep the airwaves alive on the historical frequencies (162.400 - 162.550 MHz) at zero cost to the community.

## ✨ Features
This script isn't just an audio player; it's a software architecture optimized for 24/7 broadcasting:
* **📡 Real-Time Data:** Automatically parses Environment Canada's official XML RSS feeds.
* **🗣️ Advanced TTS:** Translates text to natural-sounding voice using Google TTS.
* **⚡ Zero Latency & Zero Wear:** 100% of the audio generation happens in RAM via `BytesIO`. No SD card or hard drive writes, significantly extending hardware lifespan!
* **🎛️ Pygame Audio Engine:** Uses `Sound` objects for robust, multi-channel playback, completely preventing memory leaks and I/O closed-file errors.
* **🍁 Bilingual:** Native support for both English (`en-ca`) and French (`fr-ca`) with localized accents.

## 🛠️ Prerequisites

### Hardware
1. A PC or Raspberry Pi connected to the internet.
2. A commercial-certified VHF radio (e.g., Motorola, Kenwood) capable of sustaining a high duty cycle.
3. An audio/PTT interface (e.g., SignaLink USB or a custom serial/GPIO PTT circuit) to link the computer to the radio's mic input.

### Software
* Python 3.8 or higher.
* Python libraries listed in `requirements.txt`.

## 🚀 Installation

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/OpenWX-Canada.git](https://github.com/YOUR_USERNAME/OpenWX-Canada.git)
   cd OpenWX-Canadairwaves alive on the historical frequencies (162.400 - 162.550 MHz) at zero cost to the community.