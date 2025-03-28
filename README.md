# Interactive Story Teller

An interactive web application designed to help kids co-create their own stories using an open-source language model. Built with Python, PyTorch, Hugging Face Transformers, and Gradio, this project demonstrates how to integrate free API calls for large text generation in a fun and educational way.

## Features

- **Interactive Story Creation:** Choose story parameters such as age range, number of characters, names, type of story, and country.
- **Dynamic Story Generation:** The language model generates the initial story and continues the tale as kids add their own ideas.
- **Open-Source LLMs:** Utilizes free, open-source models (e.g., `gpt2` or `EleutherAI/gpt-neo-125M`) from Hugging Face.
- **Web-Based Interface:** Built with Gradio for a simple, user-friendly web interface.
- **CI/CD and Code Quality:** Includes GitHub Actions for continuous integration (linting, type-checking, and testing) and configurations for mypy and ruff.
- **Docker Support:** Containerized via Docker for easy sharing and deployment.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- [Docker](https://www.docker.com/) (if you want to run the container)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/interactive-storyteller.git
   cd interactive-storyteller
