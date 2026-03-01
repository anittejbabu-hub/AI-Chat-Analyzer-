def analyze_text(message):
    message = message.lower()
    words = message.split()

    # Simple sentiment lists
    positive_words = ["happy", "good", "great", "love", "excellent"]
    negative_words = ["sad", "bad", "hate", "angry", "worst"]

    toxic_words_list = ["stupid", "idiot", "dumb"]

    # Sentiment check
    positive_count = sum(word in positive_words for word in words)
    negative_count = sum(word in negative_words for word in words)

    if positive_count > negative_count:
        sentiment = "Positive 😊"
    elif negative_count > positive_count:
        sentiment = "Negative 😡"
    else:
        sentiment = "Neutral 😐"

    # Emotion detection
    if "happy" in words:
        emotion = "Happy 😄"
    elif "sad" in words:
        emotion = "Sad 😢"
    elif "angry" in words:
        emotion = "Angry 😠"
    else:
        emotion = "Normal 🙂"

    # Toxic words detection
    toxic_found = [word for word in words if word in toxic_words_list]

    return {
        "sentiment": sentiment,
        "emotion": emotion,
        "toxic_words": toxic_found
    }