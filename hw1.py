print("Hello World")

import unittest

def classifyTriangle(a,b,c):		#the main function, a b and c being the side lenghts of the triangle
	arr = [a,b,c]					#put the side lengths into an array
	arr.sort()						#sort the array so that we can access the sides in order of length (ie arr[0] always gives us the shortest side)	
#	print("Sorted Array: {},{},{}".format(arr[0],arr[1],arr[2]))	#print the array for debugging
	if (arr[0]+arr[1])<=(arr[2]):		#check to see if the given side lengths could actually form a triangle
#		print("Not a Valid Triangle!")
		return "NotATriangle"			#if it's not a valid triangle, end the function and return "NotATriangle"
	else:
		out = ""					#if it is a valid triangle, begin to create the eventual output
	if (arr[0]*arr[0]+arr[1]*arr[1]==arr[2]*arr[2]):	#check if the triangle is right
		out += "Right "
	else:
		out += ""
	if (arr[0] == arr [1] == arr[2]):									#check for equliateral
		out += "Equilateral"
	elif (arr[0] == arr[1] or arr[1] == arr[2] or arr[0] == arr[2]):	#if not check for isoceles
		out += "Isoceles"
	else:																#if not then its scalene
		out += "Scalene"
#	print("The Triangle is " + out)	#print the result
	return out

def runClassifyTriangle(a,b,c):
	print("classifyTriangle({},{},{}) = {}".format(a,b,c,classifyTriangle(a,b,c)))
	return


#a = input("Side One: ")				#console input, for testing
#b = input("Side Two: ")
#c = input("Side Three: ")  
#runClassifyTriangle(a,b,c)


class TestTriangles(unittest.TestCase): 
	def testMyTestSet(self): 
		self.assertEqual(classifyTriangle(3,4,5),'Right Scalene','3,4,5 is a Right triangle')
		self.assertEqual(classifyTriangle(3,3,3),'Equilateral','all sides are equal to 3')
		self.assertEqual(classifyTriangle(2,2,3),'Isoceles','two sides are equal to 2')
		self.assertEqual(classifyTriangle(1,1,3),'NotATriangle','Not A Valid Triangle, 1+1<3')
		self.assertNotEqual(classifyTriangle(1,1,3),'Isoceles','Not A Valid Triangle, it should not execute this part of the code')
        

if __name__ == '__main__':
	runClassifyTriangle(1,1,3)
	runClassifyTriangle(2,2,3)
	runClassifyTriangle(3,3,3)
	runClassifyTriangle(3,4,5)
    
#   unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
	unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line