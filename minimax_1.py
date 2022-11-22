import math 
import random
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

def minimax(depth, nodeIndex, maximizingPlayer,
			values):
	if depth == 4:
		return values[nodeIndex]
	if maximizingPlayer:
		for i in range(0, 3):
			val = minimax(depth + 1, nodeIndex * 3 + i,False, values)
			best = val	
		return best
	else:
		for i in range(0, 3):
			val = minimax(depth + 1, nodeIndex * 3 + i,True, values)
			best = val
		return best
if __name__ == "__main__":
    print("The optimal value is :", minimax(0, 0, True, sample_1))
    print("The optimal value is :", minimax(0, 0, True, sample_2))
    print("The optimal value is :", minimax(0, 0, True, sample_3))
    print("The optimal value is :", minimax(0, 0, True, sample_4))
