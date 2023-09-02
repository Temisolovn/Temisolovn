from classic import Question


questionz = [
    "What is red?\n (a) Fruit\n (b) Colour\n (c) Name\n\n",
    "What is apple?\n (a) Fruit\n (b) Colour\n (c) Name\n\n",
    "What is Solomon?\n (a) Fruit\n (b) Colour\n (c) Name\n\n"
]

questions = [
    Question(questionz[0], "b"),
    Question(questionz[1], "a"),
    Question(questionz[2], "c")
]
'''
print(questions[2].answer)
'''
def ezam(questions):
    score = 0
    for i in questions:
        answer = input(i.prompt)
        if answer == i.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")

ezam(questions)