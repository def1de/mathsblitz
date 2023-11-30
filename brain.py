import quadratic
import complete_square
import pythagoras


roots,coeff,poly=quadratic.generate_polynomial()
answer1,answer2,answer3=coeff[0],coeff[1],coeff[2]
print("potato",coeff)
question1 = complete_square.creating_vertex_equation(coeff[0])
if coeff[1]>2: question2 = pythagoras.find_sides(coeff[1])
else: question2 = complete_square.creating_vertex_equation(coeff[1])
question3= complete_square.creating_vertex_equation(coeff[2])

Questions = {
  "Stage1" : [{
    "question" : question1,
    "answer" : answer1,},
    {"question" : question2,
    "answer" : answer2},
    {"question" : question3,
    "answer" : answer3}],

  "Stage2":{
      "poly" : str(poly),
      "roots" : roots 
  },

  "Stage3":{
      "question" : [],
      "answer" : []
  }
}

print(Questions)

#print (poly)
#print(roots)
#xVertex,yVertex = complete_square.finding_vertex(coeff)
#print(xVertex,yVertex)