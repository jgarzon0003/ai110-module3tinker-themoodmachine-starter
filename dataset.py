"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "I feel awful today",
    "The movie made was boring, it was relaxed "
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    "negative",  # "I feel awful today"
    "mixed",  # "The movie made was boring, it was relaxed "
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)

def add_post(post, label):
    """Append a post/label pair, but only if the lists are currently aligned."""
    if len(SAMPLE_POSTS) != len(TRUE_LABELS):
        raise ValueError(
            f"SAMPLE_POSTS ({len(SAMPLE_POSTS)}) and TRUE_LABELS "
            f"({len(TRUE_LABELS)}) are out of sync; fix them before adding more."
        )
    SAMPLE_POSTS.append(post)
    TRUE_LABELS.append(label)


add_post("Lowkey stressed but kind of happy with myself", "mixed")  # stressed + happy
add_post("no cap this is an amazing day :)", "positive")  # amazing
# sarcasm — "love" + "terrible" reads mixed by word count, but the tone is fully negative
add_post("I absolutely love how terrible this traffic is", "negative")
add_post("highkey tired but the concert was so fun 😂", "mixed")  # tired + fun
# edge case: no list words present, tone is genuinely ambiguous
add_post("i guess today happened", "neutral")
add_post("missing my dog so much, feeling sad rn 🥲", "negative")  # sad
# edge case: no list words present, relief vs. exhaustion is hard to call
add_post("just finished the exam, no thoughts head empty", "neutral")
add_post("this meeting was so boring, could've been an email 💀", "negative")  # boring
add_post("weirdly relaxed even though everything feels bad right now", "mixed")  # relaxed + bad
