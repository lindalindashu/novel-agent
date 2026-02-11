import { useState } from "react"
import DiaryTab from "./components/DiaryTab"
import EntriesHistory from "./components/EntriesHistory"
import "./index.css"

function App() {
  const [activeTab, setActiveTab] = useState<'write' | 'history'>('write')

  return (
    <div className="container">
      <div className="header">
        <h1>📖 Chronicle Weaver</h1>
        <p>Transform your conversations into literary diary entries powered by AI</p>
      </div>

      <div className="tabs">
        <button
          className={`tab ${activeTab === 'write' ? 'active' : ''}`}
          onClick={() => setActiveTab('write')}
        >
          ✍️ Write New Entry
        </button>
        <button
          className={`tab ${activeTab === 'history' ? 'active' : ''}`}
          onClick={() => setActiveTab('history')}
        >
          📚 View Chronicle
        </button>
      </div>

      <div className="content">
        {activeTab === 'write' && <DiaryTab />}
        {activeTab === 'history' && <EntriesHistory />}
      </div>
    </div>
  )
}

export default App
