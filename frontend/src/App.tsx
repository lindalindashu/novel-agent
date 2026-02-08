import DiaryTab from "./components/DiaryTab"
import "./index.css"

function App() {
  return (
    <div className="container">
      <div className="header">
        <h1>📖 Chronicle Weaver</h1>
        <p>Transform your conversations into literary diary entries powered by AI</p>
      </div>

      <div className="content">
        <DiaryTab />
      </div>
    </div>
  )
}

export default App
