import mathsapi.quadratic as quadratic
import mathsapi.polynomials as polynomials
import mathsapi.pythagoras as pythagoras
import mathsapi.determinant as determinant
import mathsapi.simultaneous_equation as simultaneous_equation
import mathsapi.integration as integration
import schedule
import time
import threading
import random


used_conditions = set()


def random_question(coeff):
    global used_conditions
    available_conditions = {1, 2, 3, 4, 5} - used_conditions

    if not available_conditions:
        used_conditions = set()
        available_conditions = {1, 2, 3, 4, 5}

    random_condition = random.choice(list(available_conditions))

    if random_condition == 1:
        used_conditions.add(1)
        return polynomials.creating_vertex_equation(coeff)
    if random_condition == 2:
        if coeff > 15:
            return None
        else:
            used_conditions.add(2)
            return determinant.create_matrix_with_determinant(coeff)
    if random_condition == 3:
        used_conditions.add(3)
        random_integral = random.randint(1, 100)
        if random_integral > 0 and random_integral < 80:
            return integration.create_easy_linear_integral(coeff)
        else:
            return integration.create_hard_linear_integral(coeff)
    if random_condition == 4:
        used_conditions.add(4)
        return simultaneous_equation.simultaneous_equation(coeff)
    if (
        random_condition == 5
        and coeff > 2
        and coeff < 20
        and pythagoras.check_pythagoras(coeff)
    ):
        used_conditions.add(5)
        return pythagoras.find_sides(coeff)
    else:
        return None


def get_json():
    roots, coeff = quadratic.generate_polynomial()
    print("Coefficients: ", coeff)

    question1 = random_question(coeff[0])
    while question1 == None:
        question1 = random_question(coeff[0])

    question2 = random_question(coeff[1])
    while question2 == None:
        question2 = random_question(coeff[1])

    question3 = random_question(coeff[2])
    while question3 == None:
        question3 = random_question(coeff[2])

    final_question, final_answer = polynomials.integral(roots[0], roots[1])
    print("Final Question: ", final_question)

    questions = {
        "Stage1": [
            {
                "question": str(question1),
            },
            {
                "question": str(question2),
            },
            {
                "question": str(question3),
            },
        ],
        "Stage3": {
            "question": final_question,
        },
    }

    ans_roots = sorted(list(roots))
    answers = []
    answers += [str(i) for i in coeff]
    answers += [str(i) for i in ans_roots]
    answers += [str(final_answer)]

    return questions, answers


questions = None
answers = None


def get_questions():
    global questions
    return questions


def get_answers():
    global answers
    return answers


def update_json():
    global questions
    global answers
    questions, answers = get_json()
    print("Updated JSON")


update_json()
schedule.every().day.at("00:00").do(update_json)


def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.daemon = True
scheduler_thread.start()

if __name__ == "__main__":
    while True:
        time.sleep(10)
