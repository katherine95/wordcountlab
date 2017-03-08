def words(a):
  '''count number of times a word occurs in a string'''
  #assigns every word(key) in the dictionary with a value 
	count=dict()
	#splits the words in the string a and stores in the variable words
	words=a.split()
	#for x(every word) in words
	for x in words:
	  #counts x and gives value(number of times occured(+1)) if there is no word gives none
		count[x]=count.get(x, 0)+1
		#return every word(x) with the value
	return count
#a is the string given
a=("olly olly in come free in my in dog")	