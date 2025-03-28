# Interactive Story Teller

An interactive web application that helps kids co-create their own stories using the OpenAI API. Built with Python, Gradio, and the latest OpenAI client interface, this project demonstrates how to build a fun, interactive tool while following best practices in software development.

## Features

- **Interactive Story Creation:** Customize parameters such as age range, number of characters, names, story type, and country.
- **Dynamic Story Generation:** Uses the OpenAI API (with the cost-effective "gpt-4" model) to generate and continue stories based on user input.
- **Modern API Integration:** Leverages the new OpenAI client interface for cleaner and more robust API calls.
- **User-Friendly Interface:** Built with Gradio, providing an intuitive UI for kids and educators.
- **CI/CD and Code Quality:** Configured with GitHub Actions for continuous integration (linting, type-checking, and testing) and includes tools like mypy and ruff.
- **Docker Support:** Easily containerize and deploy the project with Docker.

## Getting Started

### Prerequisites

- **Python:** Version 3.10 or higher.
- **GitHub Personal Access Token:** Ensure your token has the `workflow` scope if you need to update GitHub Actions workflows.
- **OpenAI API Key:** Obtain one from [OpenAI](https://platform.openai.com/) and set it in your environment.
- **Docker:** (Optional) If you plan to run the application inside a container.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Paulino-Cristovao/interactive-storyteller.git
   cd interactive-storyteller
