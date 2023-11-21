import time

def ask_question(question, choices):
    print(question)
    for i, choice in enumerate(choices, start=1):
        print(f"{i} - {choice}")

    while True:
        user_answer = input("What's your answer? \n")
        try:
            user_answer = int(user_answer)
            if 1 <= user_answer <= len(choices):
                return user_answer
            else:
                print(f"Please enter a number between 1 and {len(choices)}.\n")
        except ValueError:
            print("Please enter a valid number.\n")
        except IndexError:
            print(f"Please enter a number between 1 and {len(choices)}.\n")

def main():
    print("Welcome to Trivia Challenge!")

    questions = [
        {
            'question': "Let's say you turn state's evidence and need to 'get on the lamb.' If you wait too long, what will happen?",
            'choices': ["You'll get sheep", "You'll get cow", "You'll get goat", "You'll get emu"],
            'correct_answer': 1,
            'explanation': "Getting 'on the lamb' means you'll be on the run. The correct answer is: You'll get sheep."
        }
        
    ]

    correct_answers = 0

    for question in questions:
        try:
            user_answer = ask_question(question['question'], question['choices'])
            if user_answer == question['correct_answer']:
                print("Correct!\n")
                correct_answers += 1
            else:
                print(f"Wrong! {question['explanation']}\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

        time.sleep(1)  

if __name__ == "__main__":
    main()
