# Python3 program for the above approach
	
# Initial size of
# the Array
Max = 5

# Array for the stack
# implementation
arr = [0]*Max

# Stores the minimum
# Element of the stack
minEle = 0

# Stores the top element
# of the stack
Top = 0

# Method to check whether
# stack is empty or not
def empty():

	if (Top <= 0):
		return True
	else:
		return False

# Method to push elements
# to the Special Stack
def push(x):
	global arr, Top, Max, minEle
	
	# If stack is empty
	if empty():
	
		# Assign x to minEle
		minEle = x

		# Assign x to arr[top]
		arr[Top] = x

		# Increment top by 1
		Top+=1
	# If array is full
	elif (Top == Max):

		# Update the Max size
		Max = 2 * Max

		temp = [0]*Max

		# Traverse the array arr[]
		for i in range(Top):
			temp[i] = arr[i]

		# If x is less than minEle
		if (x < minEle):
			# Push 2*x-minEle
			temp[Top] = 2 * x - minEle

			# Assign x to minEle
			minEle = x

			Top+=1
		# Else
		else:
			# Push x to stack
			temp[Top] = x
			Top+=1
		# Assign address of the
		# temp to arr
		arr = temp
	else:
		# If x is less
		# than minEle
		if (x < minEle):
			# Push 2*x-minEle
			arr[Top] = 2 * x - minEle
			Top+=1

			# Update minEle
			minEle = x
		else:
			# Push x to the
			# stack
			arr[Top] = x
			Top+=1

# Method to pop the elements
# from the stack.
def pop():
	global Top, minEle

	# If stack is empty
	if empty():
		print("Underflow")
		return
	
	# Stores the top element
	# of the stack
	t = arr[Top - 1]

	# If t is less than
	# the minEle
	if (t < minEle) :
		# Pop the minEle
		print("Popped element :", minEle)

		# Update minEle
		minEle = 2 * minEle - t
	# Else
	else:
		# Pop the topmost element
		print("Popped element :", t)
	Top-=1
	return

# Method to find the topmost
# element of the stack
def peek():
	# If stack is empty
	if empty():
		print("Underflow")
		return -1

	# Stores the top element
	# of the stack
	t = arr[Top - 1]

	# If t is less than
	# the minEle
	if (t < minEle):
		return minEle
	# Else
	else:
		return t

# Method to find the Minimum
# element of the Special stack
def getMin():
	# If stack is empty
	if empty():
		print("Underflow")
		return -1
	
	# Else
	else:
		return minEle

push(10)
push(4)
push(9)
push(6)
push(5)

print("Top Element :", peek())

print("Minimum Element :", getMin())

pop()
pop()
pop()
pop()

print("Top Element :", peek())
print("Minimum Element :", getMin())

# This code is contributed by mukesh07.
