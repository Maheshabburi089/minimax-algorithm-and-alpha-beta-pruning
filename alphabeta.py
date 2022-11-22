MAX, MIN = 1000, -1000
def minimax(depth, nodeIndex, maximizingPlayer,
			values, alpha, beta):
	if depth == 2:
		return values[nodeIndex]
	if maximizingPlayer:	
		best = MIN
		for i in range(0, 1):			
			val = minimax(depth + 1, nodeIndex * 3 + i,
						False, values, alpha, beta)
			best = max(best, val)
			alpha = max(alpha, best)
			if beta <= alpha:
				break		
		return best
	
	else:
		best = MAX
		for i in range(0, 1):		
			val = minimax(depth + 1, nodeIndex * 3 + i,
							True, values, alpha, beta)
			best = min(best, val)
			beta = min(beta, best)
			if beta <= alpha:
				break
		return best
if __name__ == "__main__":
 values = [3,12,8,2,4,6,14,5,2]
 print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX))
	
