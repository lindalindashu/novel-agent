import React, { useState } from 'react'

interface Entry {
  id: number
  user_id: number
  raw_input: string
  generated_diary: string
  created_at: string
  metadata: Record<string, any>
}

export default function DiaryTab() {
  const [input, setInput] = useState('')
  const [currentEntry, setCurrentEntry] = useState<Entry | null>(null)
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
        body: JSON.stringify({ input, username: 'default' })
      })

      const data = await response.json()

      if (response.ok) {
        setCurrentEntry(data.entry)
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
        body: JSON.stringify({ input, feedback, username: 'default' })
      })

      const data = await response.json()

      if (response.ok) {
        setCurrentEntry(data.entry)
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
    alert(`✓ Entry #${currentEntry?.id} saved to your chronicle!`)
  }

  const clearDiary = () => {
    setInput('')
    setCurrentEntry(null)
    setShowRefinement(false)
  }

  const formatDate = (dateString: string) => {
    const date = new Date(dateString)
    return date.toLocaleString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    })
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
          <button
            className="btn-primary"
            onClick={generateDiary}
            disabled={loading}
          >
            ✨ Transform to Diary
          </button>
          <button className="btn-secondary" onClick={clearDiary}>
            Clear
          </button>
        </div>
      </div>

      {loading && (
        <div className="loading active">
          <span className="spinner">⏳</span> Generating your diary entry with context...
        </div>
      )}

      {currentEntry && (
        <>
          <div className="entry-meta">
            <span>Entry #{currentEntry.id}</span>
            <span>{formatDate(currentEntry.created_at)}</span>
          </div>

          <div
            ref={outputRef}
            className="output"
          >
            {currentEntry.generated_diary}
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
                <button
                  className="btn-primary"
                  onClick={refineDiary}
                  disabled={loading}
                >
                  🔄 Regenerate
                </button>
                <button className="btn-secondary" onClick={acceptDiary}>
                  ✓ Accept
                </button>
              </div>
            </div>
          )}
        </>
      )}

      {!currentEntry && !loading && (
        <div className="output empty">
          Your diary entry will appear here...
        </div>
      )}
    </div>
  )
}
