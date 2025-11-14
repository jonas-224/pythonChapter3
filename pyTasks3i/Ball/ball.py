import random
import time

def display_welcome():
    """Display a welcome banner for the Magic 8-Ball."""
    print("═══════════════════════════")
    print("MAGIC 8-BALL FORTUNE TELLER")
    print("═══════════════════════════\n")

def get_question():
    """Prompt the user for a yes/no question and return it."""
    return input("Ask a yes/no question: ")

def get_fortune():
    """Return a random fortune from a list of possible answers."""
    answers = [
        "Without a doubt!",
        "Ask again later.",
        "Yes – definitely.",
        "My sources say no.",
        "Outlook not so good.",
        "Signs point to yes.",
        "Don't count on it.",
        "Reply hazy, try again.",
        "It is certain.",
        "Better not tell you now.",
        "Absolutely!",
        "Very doubtful."
    ]
    return random.choice(answers)
def display_fortune(fortune):
    """Display the fortune in a stylized format."""
    print(f"🔮 The Magic 8-Ball says: \"{fortune}\"\n")

def main():
    display_welcome()
    question_count = 0

    while True:
        question = get_question()
        if not question.strip().endswith("?"):
            print("Oops! Please make sure your question ends with a '?'\n")
            continue

        print("\nShaking the Magic 8-Ball", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="")
        print("\n")

        fortune = get_fortune()
        display_fortune(fortune)
        question_count += 1

        response = input("Ask another question? (yes/no): ").strip().lower()
        if response != "yes":
            break

    print(f"\nYou asked {question_count} question{'s' if question_count != 1 else ''}. Thanks for playing!")

main()

