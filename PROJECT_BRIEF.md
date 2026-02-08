# Project Brief: Chronicle Weaver

**Vision:** An intelligent AI Agent that transforms casual, fragmented daily thoughts into a cohesive, high-quality literary narrative.

---

## 1. Executive Summary

Chronicle Weaver acts as a **"Ghostwriter in the Cloud."** It bridges the gap between mundane reality and literary art by capturing life events via natural dialogue and reframing them into a serialized, novelistic diary. Unlike standard journaling apps, it focuses on narrative continuity, style mimicry, and long-term memory.

## 2. Core Value Proposition

* **Zero-Friction Journaling:** No more staring at a blank page. Users "vent" or chat; the AI handles the prose, structure, and pacing.
* **Narrative Continuity:** The agent acts as a historian, tracking recurring characters, locations, and ongoing "plot lines" to ensure a single, evolving story.
* **Literary Immersion:** Users live their lives as characters in a personalized story, choosing the tone and depth of the narrative (e.g., Noir, Magical Realism, or Minimalism).

---

## 3. Key Feature Pillars

### 🖋️ The Narrative Engine (MVP)

* **Conversational Intake:** A chat-based interface for low-pressure daily updates.
* **Refinement Loop:** An iterative process where users provide feedback (e.g., *"Make this part more dramatic"*), and the AI regenerates the prose while maintaining context.

### 🧠 Memory & Narrative Logic (High Priority)

* **Persistent History:** A robust backend that stores every interaction, allowing for deep chronological recall.
* **World State Tracking:** A "Cast of Characters" and "Atlas of Places" to ensure that your friend "Mark" or your favorite "Blue Cafe" remains consistent across entries.
* **Semantic Retrieval:** Pulling relevant context from months ago to inform today’s story (e.g., referencing a previous conflict during a new resolution).

### 🎭 Style Mimicry (Planned)

* **Author Personas:** A library of stylistic presets (e.g., Haruki Murakami, Ernest Hemingway, Jane Austen).
* **Custom Voices:** The ability for the AI to learn and adapt to the user’s unique writing voice over time.

---

## 4. High-Level Implementation Architecture

The system is designed as a **Stateful Narrative Pipeline**, where user input is enriched by historical context before reaching the LLM.

### 🏗️ Technical Logic Flow

1. **Ingestion:** User submits casual text via React frontend or CLI.
2. **Context Retrieval:** * **Recency:** The system fetches the last 3–5 entries from the relational database.
* **Entities:** The system performs a lookup on the "World State" to identify mentioned people or ongoing plot points.


3. **Augmented Prompting:** The LLM receives a "Mega-Prompt" containing the raw input, the active style profile, and the retrieved context.
4. **Generation & Storage:** The LLM outputs the prose; the system saves both the raw input and the generated narrative to maintain the chain of memory.

### 🛠️ Strategic Tech Stack

* **Intelligence:** Claude 3.5/4.1 (Optimized for high-reasoning narrative structure and nuance).
* **State Management:**
  * **Relational (SQLite):** For structured data like dates, entry IDs, and user settings.
  * **Vector Storage (ChromaDB/Pinecone):** For "semantic memory"—finding entries based on mood or themes rather than keywords.


* **Application Logic:** Python (Flask/FastAPI) to manage the orchestration between the database and the LLM.

---

## 5. Data Model Strategy

To ensure consistency, the implementation prioritizes three core data objects:

| Object | Purpose | Implementation Detail |
| --- | --- | --- |
| **The Chronicle** | The "Final" Story | Long-form text stored with metadata (date, mood, style used). |
| **The Codex** | Entity Tracking | A dictionary of People, Places, and Objects with descriptions and "Last Seen" timestamps. |
| **The Thread** | Narrative Arcs | Tags that group entries into "Plot Lines" (e.g., "The Promotion Quest" or "Summer in Paris"). |

---

## 6. Product Roadmap

| Phase | Milestone | Focus |
| --- | --- | --- |
| **Phase 1** | **The Narrative Core** | Functional MVP: API integration, basic prose generation, and refinement loops. |
| **Phase 2** | **Memory & Consistency** | **(Current Focus)** Database integration, long-term context injection, and entity tracking. |
| **Phase 3** | **Style & Voice** | Implementation of the Style Library, author mimicry, and user-defined prose preferences. |
| **Phase 4** | **Intelligence Layer** | Vector-based "Long-term Memory" for deep semantic connections across years of entries. |
