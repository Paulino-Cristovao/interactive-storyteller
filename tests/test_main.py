import re
from main import start_story, continue_story

def test_start_story():
    story = start_story("6-8", 2, "Alice, Bob", "adventure", "Wonderland")
    assert isinstance(story, str)
    # Check that the story begins with "Once upon a time"
    assert re.search(r"Once upon a time", story, re.IGNORECASE)

def test_continue_story():
    initial_story = "Once upon a time, there was an adventure."
    user_addition = "Then, a new challenge appeared."
    updated_story = continue_story(initial_story, user_addition)
    assert isinstance(updated_story, str)
    # The updated story should contain the new segment generated.
    assert "challenge" in updated_story.lower()
