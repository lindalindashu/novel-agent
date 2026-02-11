import React, { useState, useEffect } from 'react'

interface Entry {
  id: number
  user_id: number
  raw_input: string
  generated_diary: string
  created_at: string
  metadata: Record<string, any>
}

export default function EntriesHistory() {
  const [entries, setEntries] = useState<Entry[]>([])
  const [loading, setLoading] = useState(false)
  const [selectedEntry, setSelectedEntry] = useState<Entry | null>(null)
  const [limit, setLimit] = useState(10)

  const fetchEntries = async () => {
    setLoading(true)
    try {
      const response = await fetch(`/api/entries?username=default&limit=${limit}`)
      const data = await response.json()

      if (response.ok) {
        setEntries(data.entries)
      } else {
        alert('Error: ' + (data.error || 'Failed to fetch entries'))
      }
    } catch (error) {
      alert('Error: ' + (error instanceof Error ? error.message : 'Unknown error'))
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchEntries()
  }, [limit])

  const deleteEntry = async (id: number) => {
    if (!confirm(`Delete entry #${id}?`)) return

    try {
      const response = await fetch(`/api/entries/${id}`, {
        method: 'DELETE'
      })

      if (response.ok) {
        setEntries(entries.filter(e => e.id !== id))
        if (selectedEntry?.id === id) {
          setSelectedEntry(null)
        }
        alert('Entry deleted successfully')
      } else {
        alert('Failed to delete entry')
      }
    } catch (error) {
      alert('Error: ' + (error instanceof Error ? error.message : 'Unknown error'))
    }
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

  const getPreview = (text: string, length = 100) => {
    return text.length > length ? text.substring(0, length) + '...' : text
  }

  return (
    <div className="history-container">
      <div className="history-header">
        <h2><span>📚</span> Your Chronicle</h2>
        <div className="history-controls">
          <select value={limit} onChange={(e) => setLimit(Number(e.target.value))}>
            <option value={10}>Last 10</option>
            <option value={25}>Last 25</option>
            <option value={50}>Last 50</option>
            <option value={999}>All</option>
          </select>
          <button className="btn-secondary" onClick={fetchEntries}>
            🔄 Refresh
          </button>
        </div>
      </div>

      {loading && (
        <div className="loading active">
          <span className="spinner">⏳</span> Loading entries...
        </div>
      )}

      {!loading && entries.length === 0 && (
        <div className="empty-state">
          <p>📭 No entries yet. Start writing your story!</p>
        </div>
      )}

      {!loading && entries.length > 0 && (
        <div className="entries-grid">
          <div className="entries-list">
            {entries.map(entry => (
              <div
                key={entry.id}
                className={`entry-card ${selectedEntry?.id === entry.id ? 'selected' : ''}`}
                onClick={() => setSelectedEntry(entry)}
              >
                <div className="entry-card-header">
                  <span className="entry-id">#{entry.id}</span>
                  <span className="entry-date">{formatDate(entry.created_at)}</span>
                </div>
                <div className="entry-preview">
                  {getPreview(entry.generated_diary.replace(/\*\*/g, '').replace(/\n/g, ' '))}
                </div>
              </div>
            ))}
          </div>

          {selectedEntry && (
            <div className="entry-detail">
              <div className="entry-detail-header">
                <h3>Entry #{selectedEntry.id}</h3>
                <button
                  className="btn-danger"
                  onClick={() => deleteEntry(selectedEntry.id)}
                >
                  🗑️ Delete
                </button>
              </div>
              <div className="entry-meta">
                <span>{formatDate(selectedEntry.created_at)}</span>
              </div>
              <div className="entry-content">
                <h4>Generated Diary:</h4>
                <div className="diary-text">{selectedEntry.generated_diary}</div>
                <h4>Original Input:</h4>
                <div className="raw-text">{selectedEntry.raw_input}</div>
              </div>
            </div>
          )}
        </div>
      )}

      {!loading && entries.length > 0 && (
        <div className="entries-stats">
          <p>Total entries: {entries.length}</p>
        </div>
      )}
    </div>
  )
}
