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
        "answer": str(answer1)
      },
      {
        "question": str(question2),
        "answer": str(answer2)
      },
      {
        "question": str(question3),
        "answer": str(answer3)
      }
    ],
    "Stage2": {
      "poly": str(poly),
      "roots": sorted(list(roots))
    },
    "Stage3": {
      "question": final_question,
      "answer": final_answer
    }
  }
  
  return questions

result = None

def get_result():
  global result
  return result

def update_json():
  global result
  result = get_json()
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