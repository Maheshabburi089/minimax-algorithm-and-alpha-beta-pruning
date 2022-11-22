import math 
import ramdom
sample_1=[]
sample_2=[]
sample_3=[]
sample_4=[]
leaf_nodes=81 #81 leaf nodes for 4 ply game tree
for i in range(leaf_nodes):
    sample_1.append(random.randint(-15, 18))
    sample_2.append(random.randint(-10, 12))
    sample_3.append(random.randint(-9, 15))
    sample_4.append(random.randint(-12, 9))

print("sample 1:", sample_1)
print("sample 2:", sample_2)
print("sample 3:", sample_3)
print("sample 4:", sample_4)
MAX, MIN = 1000, -1000
def minimax(depth, nodeIndex, maximizingPlayer,
			values, alpha, beta):
	if depth == 4:
		return values[nodeIndex]
	if maximizingPlayer:	
		best = MIN
		for i in range(0, 3):			
			val = minimax(depth + 1, nodeIndex * 3 + i,
						False, values, alpha, beta)
			best = max(best, val)
			alpha = max(alpha, best)
			if beta <= alpha:
				break		
		return best
	
	else:
		best = MAX
		for i in range(0, 3):		
			val = minimax(depth + 1, nodeIndex * 3 + i,
							True, values, alpha, beta)
			best = min(best, val)
			beta = min(beta, best)
			if beta <= alpha:
				break
		return best
if __name__ == "__main__":
    print("The optimal value is :", minimax(0, 0, True, sample_1, MIN, MAX))
    print("The optimal value is :", minimax(0, 0, True, sample_2, MIN, MAX))
    print("The optimal value is :", minimax(0, 0, True, sample_3, MIN, MAX))
    print("The optimal value is :", minimax(0, 0, True, sample_4, MIN, MAX))
	
