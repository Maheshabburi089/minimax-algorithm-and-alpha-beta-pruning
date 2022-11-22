import math
import random 
def minimax(depth, nodeIndex, maximizingPlayer,
			values):
	if depth == 2:
		return values[nodeIndex]
	if maximizingPlayer:
		for i in range(0, 1):
			val = minimax(depth + 1, nodeIndex * 3 + i,False, values)
			best = val	
		return best
	else:
		for i in range(0, 1):
			val = minimax(depth + 1, nodeIndex * 3 + i,True, values)
			best = val
		return best
if __name__ == "__main__":
 values = [3,12,8,2,4,6,14,5,2]
 print("The optimal value is :", minimax(0, 0, True, values))
	
