def mysum(down,up):
	''' sum of down to up '''
	sum=0
	print(down)
	if down>up:
		return 0
	else:
		sum=down+mysum(down+1,up)
		print("  %d" % sum)
		return sum

if __name__=="__main__":
	print(mysum(0,100))
