#input string
def words(string):
  Dict = {}#change string to dictionary
  strsplit = string.split()#split dictionary to individual keys/word
  if len(strsplit) == 1:#if length of the word in the dictionary is one return the word
    Dict[strsplit[0]] = 1
    return Dict
  else:
    for word in strsplit:
      if word.isdigit():#if word in the dictionary is an integer return number 
        word = int(word)
      Dict[word] = strsplit.count(str(word))#change input(number) to string
    return Dict  

