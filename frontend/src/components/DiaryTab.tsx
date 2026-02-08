import React, { useState } from 'react'

export default function DiaryTab() {
  const [input, setInput] = useState('')
  const [diary, setDiary] = useState('')
  const [loading, setLoading] = useState(false)
  const [showRefinement, setShowRefinement] = useState(false)
  const [feedback, setFeedback] = useState('')
  const outputRef = React.useRef<HTMLDivElement>(null)

  const generateDiary = async () => {
    if (!input.trim()) {
      alert('Please enter some text first!')
      return
    }

    setLoading(true)
    setShowRefinement(false)

    try {
      const response = await fetch('/api/diary', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ input })
      })

      const data = await response.json()

      if (response.ok) {
        setDiary(data.diary)
        setShowRefinement(true)
        setFeedback('')
        outputRef.current?.scrollIntoView({ behavior: 'smooth', block: 'nearest' })
      } else {
        alert('Error: ' + (data.error || 'Failed to generate diary'))
      }
    } catch (error) {
      alert('Error: ' + (error instanceof Error ? error.message : 'Unknown error'))
    } finally {
      setLoading(false)
    }
  }

  const refineDiary = async () => {
    if (!feedback.trim()) {
      alert('Please provide feedback!')
      return
    }

    setLoading(true)

    try {
      const response = await fetch('/api/diary', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ input, feedback })
      })

      const data = await response.json()

      if (response.ok) {
        setDiary(data.diary)
        setFeedback('')
      } else {
        alert('Error: ' + (data.error || 'Failed to regenerate diary'))
      }
    } catch (error) {
      alert('Error: ' + (error instanceof Error ? error.message : 'Unknown error'))
    } finally {
      setLoading(false)
    }
  }

  const acceptDiary = () => {
    setShowRefinement(false)
    alert('✓ Diary accepted! Your entry is ready.')
  }

  const clearDiary = () => {
    setInput('')
    setDiary('')
    setShowRefinement(false)
  }

  return (
    <div>
      <div className="section">
        <h2><span>📝</span> Your Story</h2>
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your conversation, thoughts, or notes here..."
        />
        <div className="button-group">
          <button className="btn-primary" onClick={generateDiary}>
            ✨ Transform to Diary
          </button>
          <button className="btn-secondary" onClick={clearDiary}>
            Clear
          </button>
        </div>
      </div>

      {loading && (
        <div className="loading active">
          <span className="spinner">⏳</span> Generating your diary...
        </div>
      )}

      <div
        ref={outputRef}
        className={`output ${!diary ? 'empty' : ''}`}
      >
        {diary || 'Your diary entry will appear here...'}
      </div>

      {showRefinement && (
        <div className="refinement">
          <h3>🔄 Refine Your Entry</h3>
          <textarea
            value={feedback}
            onChange={(e) => setFeedback(e.target.value)}
            placeholder="What would you like to change? (e.g., 'Make it more emotional', 'Focus on the adventure aspect')"
          />
          <div className="button-group">
            <button className="btn-primary" onClick={refineDiary}>
              🔄 Regenerate
            </button>
            <button className="btn-secondary" onClick={acceptDiary}>
              ✓ Accept
            </button>
          </div>
        </div>
      )}
    </div>
  )
}
