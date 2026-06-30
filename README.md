[ Switch to master branch ]
# 🎙️ VoiceChat — Real-Time TCP Chat + Voice 


A lightweight **real-time chat application** built from scratch using Python's `socket` and `threading` libraries — no frameworks, no dependencies. Just raw TCP networking.

Voice chat support is actively being developed and will be integrated soon!

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Networking](https://img.shields.io/badge/protocol-TCP%20%2F%20IPv4-orange)

---

## 📌 How It Works

The app follows a classic **client-server TCP architecture**:

```
 CLIENT                          SERVER
   │                                │
   │──── username (handshake) ─────▶│
   │◀─── "Connection established" ──│
   │                                │
   │──── [64-byte header] ─────────▶│  ← message length
   │──── [message bytes]  ─────────▶│  ← actual message
   │                                │
   │         (repeat...)            │
```

### Protocol Design
Every message is sent in **two parts**:
1. A **64-byte fixed-size header** — zero-padded length of the upcoming message (`zfill(64)`)
2. The **actual message bytes** — exactly as many bytes as the header declared

This prevents partial reads and ensures clean, reliable delivery over TCP.

---

## 🗂️ Project Structure

```
Voice_chat/
├── server.py       # Multi-threaded TCP server
├── client.py       # TCP client with send/receive loop
└── README.md
```

---

## ⚙️ Features

- ✅ TCP socket communication (IPv4)
- ✅ Fixed-length header protocol (`HEADER = 64`)
- ✅ Multi-client support via `threading`
- ✅ Username handshake on connection
- ✅ Custom IP or local IP selection at server startup
- ✅ Active client count tracking
- 🔄 **Voice Chat** *(in development)*

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- No external libraries required — uses only the standard library

### Run the Server

```bash
python server.py
```

You will be prompted:
```
Type 1 for custom IP / Type 2 for Local IP :
ENTER THE PORT NUMBER :
```

> **Tip:** Use `Type 2` for running locally. Use `Type 1` if you want to bind to a specific/public IP.

### Run the Client

```bash
python client.py
```

You will be prompted:
```
ENTER YOUR NAME :
```

> Make sure the `server` IP in `client.py` matches the IP the server is running on.

---

## 🔧 Configuration

| Constant     | Default        | Description                          |
|--------------|----------------|--------------------------------------|
| `HEADER`     | `64`           | Fixed byte size of the length prefix |
| `PORT`       | `5050`         | Default port (client-side)           |
| `FORMAT`     | `utf-8`        | Text encoding                        |
| `DISCONNECT` | `'Disconnect'` | Magic string to end a session        |
| `server`     | `127.0.1.1`    | Server IP address (client-side)      |

---

## 🗺️ Roadmap

- [x] TCP socket server & client
- [x] Fixed-header message protocol
- [x] Multi-threaded client handling
- [x] Username handshake
- [x] Broadcast messages to all connected clients
- [ ] **Voice chat integration** 🎙️
- [ ] Push-to-talk support
- [ ] GUI (Tkinter or web-based)
- [ ] Graceful disconnect handling (`DISCONNECT` signal)

---

## 🧠 Key Concepts Used

- **`socket.socket(AF_INET, SOCK_STREAM)`** — IPv4 TCP socket
- **`threading.Thread`** — one thread per connected client
- **`str.zfill(64)`** — zero-pads the header to exactly 64 bytes
- **`client.recv(HEADER)`** — server always reads header first, then reads exactly that many bytes

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/voice-chat`)
3. Commit your changes (`git commit -m 'Add voice chat support'`)
4. Push and open a Pull Request

---

## 👤 Author

**sakxamydv**  
GitHub: [@sakxamydv](https://github.com/sakxamydv)

---

> ⭐ Star this repo if you find it useful — more features coming soon!
