## Project Brief: Chronicle Weaver

**Concept:** An intelligent AI Agent that transforms casual, fragmented daily conversations and notes into a cohesive, high-quality diary-style novel.

### 1. Objective

To bridge the gap between mundane reality and literary art. The agent acts as a "Ghostwriter in the Cloud," capturing the user's life events via natural dialogue and reframing them into a serialized narrative.

### 2. Core Value Proposition

* **Low Friction:** No "writer's block"—users just talk or vent; the AI handles the prose.
* **Literary Immersion:** Users can live their lives as if they are characters in their favorite books.
* **Consistency:** The agent tracks recurring characters, locations, and ongoing "plot lines" from your real life.

### 3. Target Technology Stack

* **LLM:** GPT-4o or Claude 3.5 Sonnet (for superior creative writing and stylistic mimicry).
* **Framework:** LangGraph (to manage the state of the story) or CrewAI.
* **Memory:** Vector Database (ChromaDB/Pinecone) to store the "World Bible" (your friends, family, and past events).

---

## Project Milestones & Task List

### Milestone 1: The Narrative Core (The "Ghostwriter")

**Goal:** Successfully transform raw input into a generic "Diary Novel" format.

* [ ] **Task 1.1: Persona Engineering.** Design a system prompt that balances factual accuracy (not lying about what happened) with creative flair.
  - **Technical Details:**
    - Use Claude 3.5 Sonnet API with temperature=0.7 for balanced creativity
    - System prompt structure: [Diary Context] + [Emotional Tone] + [Literary Guidelines]
    - API Call: `POST /v1/messages` with model `claude-3-5-sonnet-20241022`
    - Implement prompt versioning for A/B testing different persona templates

* [ ] **Task 1.2: Information Extraction.** Build a module to extract "Entities" (who), "Events" (what), and "Emotions" (how you felt) from a messy chat transcript.
  - **Technical Details:**
    - Create extraction pipeline using Claude with structured output (JSON schema)
    - API Call: `POST /v1/messages` with tools parameter for JSON extraction
    - Schema: `{ entities: [{ name, type, role }], events: [{ action, time, significance }], emotions: [{ feeling, intensity, trigger }] }`
    - Cache system prompt using Claude Prompt Caching for cost optimization
    - Store extracted data in PostgreSQL with vector embeddings (Pinecone/ChromaDB)

* [ ] **Task 1.3: Basic Narrative Loop.** Implement a "Review & Edit" cycle where the Agent shows a draft and asks, "Did I capture the mood correctly?"
  - **Technical Details:**
    - Generate initial draft via Claude API call
    - Create feedback prompt: "Please review if this captures your intended emotion"
    - Store user feedback in memory vector database with sentiment analysis
    - Re-generate improved draft with feedback context
    - API Calls: 2x `POST /v1/messages` (generation + refinement)

### Milestone 2: Style Mimicry (The "Author's Soul")

**Goal:** Allow users to specify a Book Title or Author (e.g., *Haruki Murakami*, *Sherlock Holmes*, or *The Great Gatsby*) to dictate the prose.

* [ ] **Task 2.1: Stylistic Analysis Engine.** Create a prompt library that defines the linguistic fingerprints of famous authors (e.g., Hemingway’s brevity vs. Tolkien’s descriptions).
  - **Technical Details:**
    - Build author style database with 50+ pre-analyzed literary profiles
    - Each profile contains: `{ author, signature_patterns: [], vocabulary_freq: {}, sentence_structure: [], themes: [] }`
    - Use Claude API to generate style embeddings: `POST /v1/embeddings` (text-embedding-3-large model)
    - Store embeddings in Pinecone vector DB with metadata (author name, era, genre)
    - API Call: `POST /v1/messages` with style context injected into system prompt

* [ ] **Task 2.2: Contextual Adaptation.** Train the agent to map real-life elements to the chosen genre (e.g., if the user chooses *Harry Potter*, their boss might be described as a "Potions Master").
  - **Technical Details:**
    - Create mapping module that translates mundane elements to genre equivalents
    - API Call: `POST /v1/messages` with role-play prompt: "Translate these modern events into a [Genre] narrative"
    - Use few-shot examples in system prompt (3-5 high-quality examples of element mappings)
    - Store successful mappings in PostgreSQL for reuse
    - Implement semantic similarity search (Pinecone) to find relevant precedents

* [ ] **Task 2.3: Preference Matching.** Build a "Style Profile" for the user so the Agent remembers to always write like *Osamu Dazai* until told otherwise.
  - **Technical Details:**
    - Create user profiles table: `{ user_id, preferred_author, preferred_genre, style_params: {} }`
    - Store in PostgreSQL with vector embeddings of user's style preferences in Pinecone
    - On each generation, retrieve user profile and prepend to context window
    - API Calls: 
      - `GET /users/{id}/profile` from backend
      - `POST /v1/messages` with profile context automatically included
      - Implement cache layer (Redis) for frequently-accessed profiles

### Milestone 3: Global Narrator (The "Polyglot")

**Goal:** Support multi-language input and output while maintaining literary quality.

* [ ] **Task 3.1: Cross-Language Nuance.** Ensure that if a user speaks in "Chinglish" or mixed languages, the Agent can produce a high-quality novel in the target language (e.g., Input in Chinese  Output in the style of *Jane Austen* in English).
  - **Technical Details:**
    - Use language detection API (Google Translate API or `langdetect` library)
    - API Call: `POST /language:detectLanguage` (Google Cloud Language API)
    - Implement multi-language LLM routing:
      - For input: Use Claude with language detection to identify dominant language
      - For output: Route to appropriate language model (claude-3-5-sonnet supports 100+ languages)
    - Create language-agnostic entity extraction (works across Chinese, English, Spanish, etc.)
    - API Call: `POST /v1/messages` with multilingual system prompt variants
    - Store translations in vector DB with language pairs (zh→en, es→en, etc.)

* [ ] **Task 3.2: Cultural Adaptation.** Ensure the Agent understands cultural metaphors when translating (e.g., translating a Chinese idiom into a Western literary equivalent).
  - **Technical Details:**
    - Build cultural idiom/metaphor database: `{ source_culture, target_culture, idiom, equivalent, context }`
    - API Call: `POST /v1/messages` with cultural adaptation prompt injected
    - Use Claude's reasoning capability to map cultural concepts (e.g., "Dragon" in Chinese context → "Divine being" in Western context)
    - Implement semantic search in Pinecone for similar cultural references
    - Create cultural context vector embeddings for each language/region
    - Validate translations against native speaker profiles (Anthropic API with human feedback loop)

* [ ] **Task 3.3: Localization UI.** Support a localized interface for users to interact with their "Agent-Novel" in their native tongue.
  - **Technical Details:**
    - Backend: i18n library (e.g., `node-polyglot` for Node.js, `gettext` for Python)
    - API endpoints return language-specific responses
    - API Call: `GET /api/config?lang=zh_CN` returns localized UI strings
    - Store UI translations in PostgreSQL `i18n_strings` table with keys
    - Frontend: Use language detection from browser settings or user preference
    - API Call: `POST /v1/messages` for dynamic content in user's preferred language
    - Support RTL languages (Arabic, Hebrew) with CSS flex-direction adjustments

---

## Example of the Evolution

| Milestone | User Input | AI Output |
| --- | --- | --- |
| **M1** | "Had a coffee, felt lonely." | *Jan 25th: I sat at the cafe today. The coffee was bitter, matching the hollow feeling in my chest.* |
| **M2** | Style: **Haruki Murakami** | *The steam rose from the cup in a perfect, indifferent spiral. In the background, a radio played soft jazz. I was a man waiting for a sign that might never come.* |
| **M3** | Style: **Gabriel García Márquez** (Output: Spanish) | *Años después, frente al pelotón de fusilamiento de la rutina, recordaría aquella tarde remota en que su café se enfrió en la soledad de la barra...* |

