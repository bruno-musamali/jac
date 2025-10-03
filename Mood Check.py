import from byllm.llm { Model }

glob llm = Model(
    provider="google",                # <- use provider, not custom_provider
    model_name="gemini/gemini-flash-lite-latest",
    verbose=True
);


def make_caption(mood: str) -> str by llm(
    prompt_template="""
Write a creative, natural caption for someone feeling "{mood}".
The caption must:
- Be 7 to 15 words
- Include at least one emoji that fits the mood
- Sound like something a real person would say on social media
- Only return the caption string, nothing else
"""
);


walker MoodGenerator {
    has mood: str;
    can start with `root entry;
}

with entry:__main__ {
   moods = ["happy", "sad", "angry", "meh", "excited", "tired", "confused", "nervous", "relaxed", "bored"];
    for m in moods {
        root spawn MoodGenerator(m);
    }
}

impl MoodGenerator.start {
      caption = "";

    # safely assign
    caption = make_caption(self.mood) or "⚠️ No caption returned";


    print("=== MOOD:", self.mood, "===");
    print("Caption:", caption);
    print("");
}