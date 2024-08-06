import mathsapi.quadratic as quadratic
import mathsapi.polynomials as polynomials
import mathsapi.pythagoras as pythagoras

import schedule
import time
import threading

def get_json():
    roots, coeff, poly = quadratic.generate_polynomial()
    
    question1 = polynomials.creating_vertex_equation(coeff[0])
    question2 = pythagoras.find_sides(coeff[1]) if coeff[1] > 2 else polynomials.creating_vertex_equation(coeff[1])
    question3 = polynomials.creating_vertex_equation(coeff[2])

    answer1, answer2, answer3 = coeff[0], coeff[1], coeff[2]

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
    answers = {
        str(answer1), str(answer2), str(answer3), str(ans_roots[0]), str(ans_roots[1]), str(final_answer)
    }
    
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