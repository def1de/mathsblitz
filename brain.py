import quadratic
import complete_square
import pythagoras
import json


roots,coeff,poly=quadratic.generate_polynomial()
answer1,answer2,answer3=coeff[0],coeff[1],coeff[2]
print("potato",coeff)
question1 = complete_square.creating_vertex_equation(coeff[0])
if coeff[1]>2: question2 = pythagoras.find_sides(coeff[1])
else: question2 = complete_square.creating_vertex_equation(coeff[1])
question3= complete_square.creating_vertex_equation(coeff[2])

def get_json():
  questions = {
    "Stage1":[
        {
          "question" : str(question1),
          "answer" : str(answer1)
      },
      {
        "question" : str(question2),
        "answer" : str(answer2)
      },
      {
        "question" : str(question3),
        "answer" : str(answer3)
      }
      ],

    "Stage2":{
      "poly" : str(poly),
      "roots" : str(roots)
    },

    "Stage3":{
        "question" : [],
        "answer" : []
    }
  }
  return json.dumps(questions)

#print (poly)
#print(roots)
#xVertex,yVertex = complete_square.finding_vertex(coeff)
#print(xVertex,yVertex)