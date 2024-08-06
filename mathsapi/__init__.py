import mathsapi.quadratic as quadratic
import mathsapi.polynomials as polynomials
import mathsapi.pythagoras as pythagoras

import schedule
import time
import threading

def get_json():
    roots, coeff = quadratic.generate_polynomial()
    
    question1 = polynomials.creating_vertex_equation(coeff[0])
    question2 = pythagoras.find_sides(coeff[1]) if coeff[1] > 2 else polynomials.creating_vertex_equation(coeff[1])
    question3 = polynomials.creating_vertex_equation(coeff[2])

    final_question, final_answer = polynomials.integral(roots[0], roots[1])
    
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
            }
        ],
        "Stage3": {
            "question": final_question,
        }
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