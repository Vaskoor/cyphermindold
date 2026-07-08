# 🛡️ CypherMind
### Self-Learning AI Penetration Testing Copilot

<p align="center">
  <img src="https://raw.githubusercontent.com/yourusername/cyphermind/main/assets/logo.png" width="180" alt="CypherMind Logo"/>
</p>

<p align="center">

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.13+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116+-009688?logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-14-black?logo=next.js)
![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6?logo=typescript&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite)
![ChromaDB](https://img.shields.io/badge/VectorDB-Chroma-FF6F00)
![NVIDIA NIM](https://img.shields.io/badge/NVIDIA-NIM-76B900?logo=nvidia)

</p>

<p align="center">
<b>An autonomous AI-powered penetration testing framework that combines Reinforcement Learning, Multi-Agent Systems, Hybrid RAG, Static Analysis, Dynamic Exploitation, and Self-Play to continuously improve cybersecurity testing.</b>
</p>

---

> **⚠️ Security Notice**
>
> CypherMind is designed **only for educational purposes and authorized penetration testing**.
> Never scan or attack systems without explicit permission.
> The authors are **not responsible for misuse** of this software.

---

# 📖 Overview

CypherMind is an **AI-native penetration testing platform** that coordinates multiple autonomous security agents using **Q-Learning**.

Unlike traditional scanners that execute predefined checks, CypherMind learns which security agents work best for different environments, remembers previous successes, retrieves relevant cybersecurity knowledge using Hybrid RAG, and continuously improves through **Red Team vs Blue Team self-play**.

The platform combines:

- 🤖 Reinforcement Learning
- 🧠 Large Language Models
- 🔍 Static Code Analysis
- ⚡ Dynamic Exploitation
- 📚 Retrieval-Augmented Generation
- 🕸️ Taint Analysis
- 🔴🔵 Adversarial Self-Play
- ⭐ Human Preference Learning

into a single intelligent cybersecurity assistant.

---

# ✨ Key Features

## 🤖 Multi-Agent Swarm

CypherMind consists of specialized AI agents working collaboratively.

| Agent | Responsibilities |
|--------|-----------------|
| 🔍 Recon Agent | Information gathering and attack surface discovery |
| 🧪 SAST Agent | Static application security testing |
| 💥 Exploit Agent | Safe vulnerability validation |
| 🛠 Post-Exploit Agent | Privilege analysis & impact assessment |
| 📚 Knowledge Agent | Hybrid RAG retrieval |
| 🔴 Red Team Agent | Offensive strategy generation |
| 🔵 Blue Team Agent | Defensive reasoning & mitigation |

---

## 🧠 Reinforcement Learning Orchestrator

Instead of executing every tool sequentially, CypherMind uses **Tabular Q-Learning** to determine:

- Which agent should execute first
- Which exploit chain is most promising
- Which workflow produced the highest reward
- Which sequence should be reused

Features include:

- ε-Greedy Exploration
- Bellman Equation Updates
- Persistent Q-Table
- Adaptive Agent Scheduling

---

## 📚 Hybrid RAG

The AI assistant retrieves security knowledge using a hybrid retrieval pipeline.

Pipeline:

```
User Query
      │
      ▼
 BM25 Keyword Search
      │
      ▼
 ChromaDB Vector Search
      │
      ▼
 Candidate Merging
      │
      ▼
 Cross Encoder Re-ranking
      │
      ▼
 Best Context
      │
      ▼
 LLM Response
```

Supports:

- CVEs
- OWASP
- MITRE ATT&CK
- Internal reports
- Pentesting notes
- Previous engagements

---

## 🕸️ Static Taint Analysis

CypherMind automatically discovers dangerous data flows.

Example:

```
User Input
      │
      ▼
HTTP Request
      │
      ▼
Controller
      │
      ▼
Database Query
      │
      ▼
SQL Sink
```

Detects:

- SQL Injection
- Command Injection
- XSS
- Path Traversal
- Unsafe File Access

---

## 🔴 Red vs 🔵 Blue Self-Play

One of the most innovative components.

Two AI agents compete against each other.

```
Red Team
   │
Generate Attack
   │
   ▼
Blue Team
   │
Generate Defense
   │
   ▼
Judge
   │
Reward
   │
   ▼
RL Update
```

Benefits:

- Discovers new attack chains
- Improves defensive reasoning
- Generates training data
- Continuous autonomous learning

---

## ⭐ Human Preference Learning

CypherMind supports human feedback.

Users compare two AI-generated penetration strategies.

```
Strategy A

vs

Strategy B

↓

Human chooses best

↓

Bradley-Terry Model

↓

Preference Score Update
```

The AI gradually learns which strategies humans prefer.

---

## 📡 Real-Time Dashboard

Live WebSocket updates display:

- Active agents
- Running tasks
- Vulnerabilities found
- RL rewards
- Self-play progress
- Knowledge retrieval
- System logs

---

# 🏗 System Architecture

```
                        +---------------------------+
                        |        Frontend           |
                        |        Next.js            |
                        +------------+--------------+
                                     |
                                     |
                         REST API / WebSockets
                                     |
                                     ▼
                    +-------------------------------+
                    |        FastAPI Backend         |
                    +-------------------------------+
                                     |
     ------------------------------------------------------------------
     |             |              |             |             |         |
     ▼             ▼              ▼             ▼             ▼         ▼

Q-Learning    Multi-Agent      Hybrid RAG   Taint Graph   Self Play  Feedback
Scheduler       Swarm          Retrieval      Engine       Arena      Learning

     |             |              |             |             |
     ----------------------------------------------------------
                           |
                           ▼
                   SQLite + ChromaDB
                           |
                           ▼
                    Security Knowledge
```

---

# 🛠 Tech Stack

## Backend

- FastAPI
- Python 3.13+
- SQLAlchemy
- SQLite
- ChromaDB
- NetworkX
- asyncio
- WebSockets

---

## Frontend

- Next.js 14
- React
- TypeScript
- Tailwind CSS
- shadcn/ui
- React Query

---

## AI

- NVIDIA NIM
- Embedding Models
- Cross Encoder Re-Ranker
- Reinforcement Learning
- Bradley-Terry Ranking

---

## Security Tools

Optional integrations:

- Semgrep
- Bandit
- TruffleHog
- SQLMap
- Nuclei
- Nmap
- Nikto
- Gobuster

CypherMind automatically skips unavailable tools.

---

# 📂 Project Structure

```
CypherMind/

├── backend/
│   ├── app/
│   ├── agents/
│   ├── api/
│   ├── core/
│   ├── services/
│   ├── rl/
│   ├── rag/
│   ├── taint/
│   └── models/
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── hooks/
│   ├── lib/
│   └── public/
│
├── tests/
├── docs/
├── assets/
├── LICENSE
└── README.md
```

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/yourusername/cyphermind.git

cd cyphermind
```

---

## Backend Installation

```bash
cd backend

python -m venv .venv

source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Frontend Installation

```bash
cd frontend

npm install
```

---

# ⚙️ Environment Variables

Create

```
backend/.env
```

Example

```env
NVIDIA_API_KEY=

DATABASE_URL=sqlite:///cyphermind.db

CHROMA_PATH=./chromadb

SECRET_KEY=change_me

ENV=development
```

---

# ▶ Running

Backend

```bash
cd backend

source .venv/bin/activate

export PYTHONPATH=.

uvicorn app.main:app --reload --port 8000
```

Frontend

```bash
cd frontend

npm run dev
```

Open

```
http://localhost:3000
```

API Docs

```
http://localhost:8000/docs
```

---

# 📡 REST API

| Method | Endpoint | Description |
|----------|------------------------------|----------------|
| GET | /health | Health Check |
| GET | /api/v1/dashboard/stats | Dashboard Metrics |
| POST | /api/v1/engagements | Create Engagement |
| POST | /api/v1/agents/execute | Execute Agents |
| POST | /api/v1/selfplay/start | Start Self-Play |
| POST | /api/v1/knowledge/query | Hybrid RAG |
| WS | /ws/engagements/{id} | Live Events |

---

# 🧪 Running Tests

```bash
pytest tests -v
```

---

# 🛣 Roadmap

- [x] Multi-Agent Architecture
- [x] Q-Learning Scheduler
- [x] Hybrid RAG
- [x] Taint Analysis
- [x] WebSocket Dashboard
- [x] Self-Play Arena
- [x] Preference Learning
- [ ] PPO Reinforcement Learning
- [ ] Kubernetes Deployment
- [ ] Multi-Target Scheduling
- [ ] Distributed Agent Swarm
- [ ] Cloud Deployment
- [ ] Autonomous Exploit Chain Generation

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a branch

```bash
git checkout -b feature/amazing-feature
```

3. Commit

```bash
git commit -m "Add amazing feature"
```

4. Push

```bash
git push origin feature/amazing-feature
```

5. Open a Pull Request

---

# 📜 License

Distributed under the **MIT License**.

See the **LICENSE** file for details.

---

# 🙏 Acknowledgements

Special thanks to the open-source communities behind:

- FastAPI
- Next.js
- ChromaDB
- NVIDIA NIM
- OWASP
- MITRE ATT&CK
- Semgrep
- SQLMap
- Bandit
- Nuclei

---

# 📚 Citation

If you use CypherMind in research or academic work, please cite:

```text
CypherMind: Self-Learning AI Penetration Testing Copilot
2026
https://github.com/yourusername/cyphermind
```

---

<p align="center">

**🛡️ Secure Smarter • Learn Continuously • Hack Responsibly**

Made with ❤️ using **FastAPI**, **Next.js**, **Reinforcement Learning**, and **Artificial Intelligence**

⭐ **If you found this project useful, consider giving it a star!**

</p>