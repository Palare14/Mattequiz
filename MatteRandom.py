import random

def generate_question():
    operand1 = random.randint(1, 10)
    operand2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    question = str(operand1) + ' ' + operator + ' ' + str(operand2)
    answer = eval(question)
    return question, answer

def main():
    correct_answers = 0
    total_questions = 1000  # Endre dette tallet for å endre antall spørsmål

    print("Velkommen til mattequiz!")

    for i in range(total_questions):
        question, correct_answer = generate_question()
        user_answer = float(input("Spørsmål {}: Hva er {}? ".format(i + 1, question)))

        if user_answer == correct_answer:
            print("Riktig svar!")
            correct_answers += 1
        else:
            print("Feil svar. Riktig svar er", correct_answer)

    score = (correct_answers / total_questions) * 100
    print("Quiz avsluttet. Du fikk", correct_answers, "av", total_questions, "riktige.")
    print("Poengsum:", score, "%")

if __name__ == '__main__':
    main()
