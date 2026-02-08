# Chronicle Weaver - Vite + React Frontend

## Setup Complete! 🎉

Your frontend has been migrated from Next.js to **Vite + React + TypeScript**.

### Architecture

```
Frontend (Vite + React)     →  Flask Backend API  →  Claude API
Port 3000                       Port 8000
Direct calls to /api/diary
/api/entities
```

### What Changed

- **Removed**: Next.js full-stack setup (no more /pages/api)
- **Added**: Pure Vite + React frontend with direct Flask API calls
- **Simpler**: One clean codebase, single tech stack (JavaScript/React)
- **Faster**: Vite is faster than Next.js for development

### Project Structure

```
frontend/
├── src/
│   ├── App.tsx              (Main app component with tabs)
│   ├── components/
│   │   ├── DiaryTab.tsx     (Diary generation component)
│   │   └── EntitiesTab.tsx  (Entity extraction component)
│   ├── main.tsx             (Entry point)
│   └── index.css            (Styling)
├── index.html               (HTML entry point)
├── vite.config.ts           (Vite configuration)
├── tsconfig.json            (TypeScript config)
└── package.json             (Dependencies)

backend/
├── app.py                   (Flask server)
├── llm_service.py           (LLM logic)
├── config.py                (Configuration)
├── main.py                  (CLI tool)
└── requirements.txt         (Python deps)
```

### Getting Started

#### 1. Start the Flask Backend

```bash
cd /Users/lindashu/Desktop/agents/novel-agent/backend
python3 app.py
# Server runs on http://127.0.0.1:8000
```

#### 2. Start the Vite Frontend

```bash
cd /Users/lindashu/Desktop/agents/novel-agent/frontend
npm run dev
# Server runs on http://localhost:3000
```

#### 3. Open in Browser

Visit: **http://localhost:3000**

### Node.js Issue

If you see `Unexpected token '??='` error, your Node.js version (14.17.3) is too old.

**Solution**: Upgrade Node.js to v18+ or v20+
```bash
# Using Homebrew:
brew install node@20
```

### Features

✨ **Diary Writer Tab**
- Input conversations or notes
- Transform to literary diary entries
- Refinement loop with feedback
- Timestamps automatically added

🔍 **Entity Extractor Tab**
- Extract entities (people, places, things)
- Extract events with timeline
- Extract emotions with intensity
- Structured JSON output

### API Endpoints

The frontend calls your Flask backend:

```
POST http://127.0.0.1:8000/api/diary
  Body: { input: string, feedback?: string }
  Response: { success: true, diary: string }

POST http://127.0.0.1:8000/api/entities
  Body: { input: string }
  Response: { success: true, entities: {...} }
```

### Development Commands

```bash
# Development server (with hot reload)
npm run dev

# Build for production
npm run build

# Preview production build
npm preview
```

### Next Steps

1. **Milestone 2**: Add author style mimicry
   - Build database of 50+ author styles
   - Implement style injection into prompts
   - Add author selection in UI

2. **Milestone 3**: Multi-language support
   - Add language selection dropdown
   - Implement language detection
   - Cultural adaptation for different languages

3. **Deployment**
   - Backend: Deploy Flask to Heroku, Railway, or Vercel
   - Frontend: Deploy Vite build to Netlify, Vercel, or GitHub Pages

---

**Happy coding!** 🚀 Let me know if you hit any issues with the Vite setup.
