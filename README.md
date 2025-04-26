# 🚇 AI-Powered WhatsApp Metro Ticket Booking Bot

This project is an **AI-powered WhatsApp Metro Ticket Booking Bot** that lets users book Chennai Metro tickets via WhatsApp using text or voice. It uses n8n, OpenAI Whisper, and Twilio.

---

## ✨ Features

- Book tickets via WhatsApp (text or voice)
- Voice-to-text transcription with OpenAI Whisper
- Fuzzy matching for station names (handles typos and speech errors)
- Dynamic fare calculation (₹16, ₹24, ₹32, ₹40)
- QR code ticket generated and sent instantly
- Automated workflow using n8n

---

## 🛠️ Tech Stack

- **n8n** – Workflow automation
- **Twilio WhatsApp API** – Messaging integration
- **OpenAI Whisper** – Speech-to-text
- **Python** (Flask for Whisper server)
- **JavaScript** (for workflow logic and fuzzy matching)

---

## 🚀 How It Works

1. **User sends a WhatsApp message** (text or voice) to the Twilio number.
2. **n8n Webhook** receives the message and determines if it’s text or audio.
3. **If audio:** n8n downloads the file and sends it to the local Whisper server for transcription.
4. **Station names** are extracted and fuzzy-matched from the message.
5. **Fare is calculated** based on the number of stations crossed.
6. **A ticket ID and QR code** are generated.
7. **Ticket details and QR code** are sent back to the user on WhatsApp.

---

## 📦 Folder Structure

ai-powered-whatsapp-metro-ticket-booking/
├── workflows/
│ └── WhatsApp_Metro_Ticket_Bot.json # n8n workflow export
├── whisper-server/
│ └── whisper_server.py # Flask/Whisper API code
├── .gitignore
└── README.md

---

## 📝 Setup Instructions

1. **Clone the repository:**
git clone https://github.com/yourusername/ai-powered-whatsapp-metro-ticket-booking.git
cd ai-powered-whatsapp-metro-ticket-booking

2. **Set up the Whisper server:**
- Install Python dependencies (see [Whisper repo](https://github.com/openai/whisper))
- Run the Flask server (`whisper_server.py`)
3. **Set up n8n:**
- Import the workflow from `workflows/WhatsApp_Metro_Ticket_Bot.json`
- Configure Twilio credentials in n8n (do NOT hardcode secrets in the workflow)
- Set your webhook URL in Twilio (use ngrok if running locally)
4. **Start all services** and test by sending a WhatsApp message!

---

## ⚠️ Security Notice

- **Never commit real credentials or secrets** to the repository.
- Use n8n’s credential manager or environment variables for sensitive information.

---

## 🙌 Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper)
- [n8n](https://n8n.io/)
- [Twilio](https://www.twilio.com/)
- [QRServer](https://goqr.me/api/)

---

## 📬 Contact

Questions or feedback?  
Open an issue or reach out on [LinkedIn](https://www.linkedin.com/in/dineshk4rthick/).

---

**Happy commuting with AI! 🚇🤖**
