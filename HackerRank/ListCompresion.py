

x =1
y=1
z =1 
n= 2

def listComprension(x,y,z,n):

    finalBox = []

    for x in range(x+1):
 
        for y in range (y+1):
           
            for z in range(z+1):
                if(x+y+z==n):
                    continue
            
                finalBox.append([x,y,z])

    print(finalBox)

listComprension(x,y,z,n)


'''

Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

Example




All permutations of  are:
.

Print an array of the elements that do not sum to .


Input Format

Four integers  and , each on a separate line.

Constraints

Print the list in lexicographic increasing order.

'''