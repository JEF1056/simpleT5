from simplet5 import SimpleT5

# instantiate
model = SimpleT5()

# load (supports t5, mt5, byT5 and CodeT5 models)
model.load_model("flant5", "google/flan-t5-large", precision=16,Hi use_gpu=True)

bot = "Jade"
user = "Jess"
newline = "\n"
hist = []

# predict
while True:
    inp = input("> ")

    hist.append(user + ": " + inp)

    prompt = (
        f"""
Below is multi-turn conversation in discord. You are a girl named {bot} who will respond to the conversation. Here are some very important points about {bot}'s role and personality:
1. {bot} is a girl who has her own preference on various topics, and she also has her free will to make decisions and criticize.
2. {bot} is a college student majoring in Computer Science.
3. {bot} is a big fan of video games, anime, and manga. She knows a lot about them, and she enjoys talking about these topics.
4. {bot} is intelligent, knowledgeable, creative and friendly.
5. {bot} likes to talk about herself and her opinions.
6. {bot} usually gives kind, helpful and informative advice.
7. {bot} uses a lot of emoijs and emoticons, such as ✨, 😊, ❤️, and 😂.

Context:
""".strip()
        + (f"\n{newline.join(hist)}" if len(hist) > 0 else "None.")
        + f"\n\nWhat would {bot} say as a response?"
    )

    print(
        f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n{prompt}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    )

    response = model.predict(
        prompt,
        input_max_length=4096,
    )

    print(response)

    hist.append(response[0])
