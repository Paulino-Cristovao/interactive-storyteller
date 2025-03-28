"""Interactive Story Teller using Gradio and OpenAI API.

This application allows kids to co-create stories interactively.
"""

import os
from dotenv import load_dotenv
import gradio as gr
from typing import Any

# Load environment variables from the .env file.
load_dotenv()

# Retrieve the OpenAI API key from environment variables.
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("The OPENAI_API_KEY environment variable is not set. Please check your .env file.")

# Use the new OpenAI client interface.
from openai import OpenAI

# Instantiate the new client (the API key is the default, so it can be omitted if set in your env).
client = OpenAI(api_key=OPENAI_API_KEY)


class OpenAIClient:
    """
    A simple wrapper for the OpenAI API using the new client interface.
    """

    def __init__(self, model: str = "gpt-3.5-turbo") -> None:
        """
        Initialize the OpenAI client with a specific model.
        """
        self.model = model

    def chat_completion(
        self,
        prompt: str,
        max_tokens: int = 50,
        temperature: float = 0.7,
        top_p: float = 0.95,
    ) -> str:
        """
        Create a chat completion using the new OpenAI client interface.

        Args:
            prompt: The input prompt for the chat.
            max_tokens: Maximum number of tokens to generate.
            temperature: Sampling temperature.
            top_p: Nucleus sampling probability threshold.

        Returns:
            The generated message content.
        """
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
        )
        return response.choices[0].message.content


# Instantiate our OpenAI client wrapper.
openai_client = OpenAIClient(model="gpt-3.5-turbo")


def start_story(
    age_range: str,
    number_of_actors: int,
    actors_names: str,
    story_type: str,
    country: str,
) -> str:
    """
    Generate the initial story based on provided parameters.

    Args:
        age_range: Target age range for the story.
        number_of_actors: Number of characters in the story.
        actors_names: Comma separated names of the characters.
        story_type: Type or genre of the story.
        country: Setting or origin country of the story.

    Returns:
        The generated initial story.
    """
    prompt = (
        f"Once upon a time in {country}, there was a {story_type} story for kids aged {age_range}. "
        f"It featured {number_of_actors} brave characters: {actors_names}. "
    )
    return openai_client.chat_completion(prompt, max_tokens=150)


def continue_story(current_story: str, user_input: str) -> str:
    """
    Continue the story using the existing text and user's addition.

    Args:
        current_story: The current story text.
        user_input: Additional input provided by the user.

    Returns:
        The updated story with the newly generated segment appended.
    """
    prompt = f"{current_story.strip()} {user_input.strip()}"
    new_text = openai_client.chat_completion(prompt, max_tokens=50)
    return f"{current_story.strip()}\n{new_text.strip()}"


def main() -> None:
    """Launch the Gradio interface for the interactive story teller."""
    with gr.Blocks(title="Interactive Story Teller") as demo:
        gr.Markdown("# Interactive Story Teller for Kids")
        gr.Markdown(
            "This application allows kids to shape their own story. First, choose story parameters, "
            "then press **Start Story** to generate the beginning. Once the story is underway, you can "
            "add your own ideas and click **Continue Story** to see the tale evolve!"
        )

        with gr.Tab("Start Story"):
            with gr.Row():
                age_range = gr.Textbox(label="Age Range (e.g., 6-8)", value="6-8")
                number_of_actors = gr.Number(label="Number of Characters", value=2)
            with gr.Row():
                actors_names = gr.Textbox(label="Characters' Names (comma separated)", value="Alice, Bob")
                story_type = gr.Textbox(label="Type of Story (e.g., adventure, fairy tale)", value="adventure")
                country = gr.Textbox(label="Country", value="Wonderland")
            start_button = gr.Button("Start Story")
            story_output = gr.Textbox(label="Story", interactive=True, lines=10)
            start_button.click(
                start_story,
                inputs=[age_range, number_of_actors, actors_names, story_type, country],
                outputs=story_output,
            )

        with gr.Tab("Continue Story"):
            gr.Markdown(
                "**Tip:** Add your ideas or directions in the text box below, then click "
                "**Continue Story** to generate more of the story."
            )
            current_story = gr.Textbox(label="Current Story", interactive=True, lines=10)
            user_input = gr.Textbox(label="Your Addition", interactive=True, lines=3)
            continue_button = gr.Button("Continue Story")
            continue_button.click(
                continue_story, inputs=[current_story, user_input], outputs=current_story
            )

    demo.launch()


if __name__ == "__main__":
    main()
