import time

N = int(input(),10)
r = [[],[]]
r[0] = list(map(int,input().split()))
r[1] = list(map(int,input().split()))
diff = []	
scores = []

class score:
	def __init__(self,value = None, vertical = True ):
		self.value = value
		self.vertical = vertical


def getDominoScore(coloum,vertical):
	if (vertical):
		return (abs(r[0][coloum] - r[1][coloum]))
	else:
		return(abs(r[0][coloum] - r[0][coloum + 1] )+ abs(r[1][coloum] - r[1][coloum + 1]))

def generateScores(col):
  a = getDominoScore(col,True)
  try:
    b = getDominoScore(col,False)
  except IndexError:
    pass
  if(col==0):
    newScore = score(a)
    scores.append(newScore)
    newScore = score(b,False)
    scores.append(newScore)
    return
  elif(col<N-1):
    l = []
    for s in scores:
      if(s.vertical):
        newScore = score(s.value+b,False)
        l.append(newScore)
        s.value += a
      else:
        s.vertical = True
    scores.extend(l)
    return
  else:
    for s in scores:
      if(s.vertical):
        s.value += a
    return
        
def updateScore():
  Mv = max(list(map(lambda x: x.value,list(filter(lambda x: x.vertical,scores)))))
  Mh = max(list(map(lambda x: x.value,list(filter(lambda x: not x.vertical,scores)))))
  del scores[:]
  newScore = score(Mv)
  scores.append(newScore)
  newScore = score(Mh,False)
  scores.append(newScore)
  
start_time = time.time()
for col in range(N):
  generateScores(col)
  updateScore()
  #print(list(map(lambda x: (x.value,x.vertical),scores)))
M = max(list(map(lambda x: x.value,scores)))
print(M)
print("--- %s seconds ---" % (time.time() - start_time))

		

	
	
	
	
	
