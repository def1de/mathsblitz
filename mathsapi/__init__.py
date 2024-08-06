import mathsapi.quadratic as quadratic
import mathsapi.complete_square as complete_square
import mathsapi.pythagoras as pythagoras

def get_json():
  roots, coeff, poly = quadratic.generate_polynomial()
  answer1, answer2, answer3 = coeff[0], coeff[1], coeff[2]
  
  question1 = complete_square.creating_vertex_equation(coeff[0])
  question2 = pythagoras.find_sides(coeff[1]) if coeff[1] > 2 else complete_square.creating_vertex_equation(coeff[1])
  question3 = complete_square.creating_vertex_equation(coeff[2])
  
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
      "question": r"\[ \int_{x_1}^{x_2} (x + 2) \,dx = \]",
      "answer": []
    }
  }
  
  return questions
