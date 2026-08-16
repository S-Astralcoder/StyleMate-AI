# StyleMate AI Agent 👗✨

**StyleMate** is a personalized AI styling assistant designed to provide hyper-personalized fashion advice. By leveraging advanced LLMs, it helps you curate outfits, understand color theory, and manage your wardrobe with ease.

---

## 🚀 Features

- **Personalized Styling:** Get tailored outfit recommendations based on your existing wardrobe.
- **Color Theory Integration:** Utilizes professional color theory principles to suggest optimal palette combinations.
- **Dynamic Preference Tracking:** Actively maintains and evolves your style profile through natural conversation.
- **Modular Architecture:** Highly extensible design featuring custom agents, tools, and persistent memory.

---

## 🏗️ Project Structure

```text
src/
├── agent.py      # Core agent logic & interaction loop
├── functions.py  # Function execution & tool registry
├── goal.py       # Assistant objectives & persona definition
├── memory.py     # Conversation history & state management
├── tools.py      # Data retrieval & preference tools
└── tool/         # Implementation of specific tools
main.py           # Application entry point
pyproject.toml    # Dependencies and build configuration
```

---

## 🛠️ Getting Started

### Prerequisites

* **Python:** 3.12+
* **Package Manager:** [uv](https://github.com/astral-sh/uv) (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd stylemate-ai
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Configure environment:**
   Create a `.env` file in the root directory and add your required LLM API keys.

4. **Run the assistant:**
   ```bash
   python main.py
   ```

---

## 💡 How it works
StyleMate combines context-aware memory with a suite of styling tools to act as your digital fashion consultant. Whether you are prepping for an interview or building a capsule wardrobe, StyleMate helps you make informed choices.

---
*Built with care for better fashion choices.*
