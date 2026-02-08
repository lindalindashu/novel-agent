# 📖 Chronicle Weaver

An intelligent AI agent that transforms casual conversations and notes into beautiful, literary diary entries.

> **"Turn your everyday moments into literary art"**

---

## ✨ Features

- 🎭 **AI Ghostwriter** - Transforms casual input into eloquent diary entries
- 🔄 **Refinement Loop** - Review and refine entries with natural feedback
- 📅 **Auto-Dating** - Automatically adds formatted dates to entries
- 💬 **Natural Input** - Just talk or vent; the AI handles the prose
- 🎨 **Literary Quality** - Emotionally resonant, well-crafted narratives

---

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- Node.js 18+
- Anthropic API Key ([Get one here](https://console.anthropic.com/))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/chronicle-weaver.git
cd chronicle-weaver
```

2. **Set up backend**
```bash
cd backend
pip install -r requirements.txt

# Create .env file with your API key
echo "ANTHROPIC_API_KEY=your-key-here" > .env
```

3. **Set up frontend**
```bash
cd ../frontend
npm install
```

4. **Make scripts executable**
```bash
cd ..
chmod +x start-backend.sh
```

### Running the App

**Option 1: Web Interface**
```bash
# Terminal 1: Start backend (port 8000)
./start-backend.sh

# Terminal 2: Start frontend (port 3000)
cd frontend && npm run dev
```

Open http://localhost:3000 in your browser

**Option 2: CLI Mode**
```bash
cd backend
python3 cli.py
```

---

## 🏗️ Technology Stack

### Backend
- **LLM:** Claude Opus 4.1 (claude-opus-4-1-20250805)
- **Framework:** Flask 3.0.0 with Blueprint architecture
- **Language:** Python 3.13

### Frontend
- **Framework:** React 19.2.4 + TypeScript 5.9.3
- **Build Tool:** Vite 7.3.1
- **Styling:** Custom CSS

### API
- RESTful API with Vite proxy (no CORS needed)
- Endpoint: `POST /api/diary`

---

## 📁 Project Structure

```
chronicle-weaver/
├── backend/
│   ├── app/
│   │   ├── __init__.py       # Flask app factory
│   │   ├── config.py         # Configuration
│   │   ├── routes/
│   │   │   └── diary.py      # API endpoints
│   │   └── services/
│   │       └── llm_service.py # Claude integration
│   ├── cli.py                # Command-line interface
│   ├── run.py                # Web server entry point
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.tsx           # Main app
│   │   ├── components/
│   │   │   └── DiaryTab.tsx  # Diary UI
│   │   └── index.css
│   ├── package.json
│   └── vite.config.ts        # Vite + proxy config
│
└── PROJECT_BRIEF.md          # Detailed project documentation
```

---

## 💡 Usage Example

**Input:**
```
Had coffee with Sarah today. She told me about her new job.
I felt happy for her but also a bit envious. The cafe was crowded.
```

**Output:**
```
**February 8, 2026**

I sat across from Sarah at our usual café, the one with the worn
leather chairs and the espresso machine that hisses like a small
dragon. She spoke of her new position with an excitement that made
her eyes bright—and I was genuinely happy for her. Yet beneath my
smile, a small seed of envy took root, unwelcome and stubborn.
Around us, the café hummed with life, conversations blending into
a single warm murmur.
```

---

## 🎯 Roadmap

### ✅ Milestone 1: MVP (COMPLETED)
- [x] Basic diary generation
- [x] Refinement loop with feedback
- [x] Web UI and CLI interfaces

### 🔮 Milestone 2: Memory & Consistency (IN PROGRESS)
- [ ] **Phase 3.1:** SQLite database for persistence
  - Save and retrieve diary entries
  - Context injection from past entries
  - User preferences storage
- [ ] **Phase 3.2:** Vector database for semantic search
  - Smart context retrieval
  - Character/entity tracking
  - Timeline visualization

### 🔄 Milestone 3: Style Mimicry (PLANNED)
- [ ] Author style selection (Murakami, Hemingway, Austen, etc.)
- [ ] Style preferences per user
- [ ] Contextual adaptation to genres

### 🌍 Milestone 4: Global Narrator (FUTURE)
- [ ] Multi-language support
- [ ] Cultural adaptation
- [ ] Localized UI

---

## 🔧 Configuration

### Backend Configuration (`backend/app/config.py`)
```python
ANTHROPIC_API_KEY = "your-key-here"
MODEL = "claude-opus-4-1-20250805"
MAX_TOKENS = 2048
TEMPERATURE = 0.7
```

### Frontend Configuration
Create `frontend/.env`:
```bash
VITE_API_URL=http://127.0.0.1:8000
```


---

## 📝 License

This project is licensed under the MIT License.


