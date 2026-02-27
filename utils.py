from textblob import TextBlob

# -------------------------
# Get Response (Stage-Based Chatbot)
# -------------------------
def get_llm_response(messages):
    """
    Simple structured hiring chatbot without AI.
    Uses conversation stages.
    """

    # Count user messages (excluding system)
    user_messages = [m for m in messages if m["role"] == "user"]
    step = len(user_messages)

    user_input = user_messages[-1]["content"]

    # Step 1: Greeting
    if step == 1:
        return "Hello! Welcome to TalentScout. What is your full name?"

    # Step 2: After Name
    elif step == 2:
        return f"Nice to meet you, {user_input}! What position are you applying for?"

    # Step 3: After Position
    elif step == 3:
        return "Great! How many years of experience do you have?"

    # Step 4: After Experience
    elif step == 4:
        return "What are your primary technical skills? (e.g., Python, Java, React)"

    # Step 5: Technical Question Based on Skills
    elif step == 5:
        skills = user_input.lower()

        if "python" in skills:
            return "Explain the difference between a list and a tuple in Python."
        elif "java" in skills:
            return "What is the difference between JDK, JRE, and JVM?"
        elif "react" in skills:
            return "What is the purpose of useEffect in React?"
        else:
            return "Can you describe one challenging project you worked on?"

    # Step 6: Final Response
    elif step == 6:
        return "Thank you for your answers. Our recruitment team will review your profile and contact you soon."

    else:
        return "Thank you. The interview process is complete."


# -------------------------
# Exit Command Detection
# -------------------------
def is_exit_command(user_input):
    exit_keywords = ["exit", "quit", "bye", "goodbye", "stop", "end"]
    return user_input.strip().lower() in exit_keywords


# -------------------------
# Sentiment Analysis
# -------------------------
def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.1:
        return "Positive 🙂"
    elif polarity < -0.1:
        return "Negative 🙁"
    else:
        return "Neutral 😐"