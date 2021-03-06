# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", 
"help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", 
"distressing", "concerning", "horrible", "horribly", "questionable"]
negative_string = "I am concerned that this project is horrible, awful, and broken."
punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]

def censor_phrase(phrase,text):
  censor_word =''
  for i in range(len(phrase)):
    if phrase[i] == " ":
      censor_word += " "
    else:
      censor_word +='#'
  return text.replace(phrase,censor_word)

def censor_word(word):
  censor_word =''
  for i in range(len(word)):
    censor_word +='#'
  return censor_word

def is_censored_word(word):
	if word.find('#') > -1:
		return True
	else:
		return False

def censor_phrases_in_list(phrase_list,text):
  # Used in Question 2 of the project
  for phrase in phrase_list:
    text = censor_phrase(phrase,text)
  return text 

def clean_word(word):
  for punc in punctuation:
    word = word.strip(punc)
  return word

def is_negative_word(word):
  for i in range(len(negative_words)):
      if clean_word(word).find(negative_words[i]) > -1:
        return True
  return False

def censor_negative_and_proprietary_words(negative_string):
  # censor any occurance of a word from the “negative words” list 
  # after any “negative” word has occurred twice,
  # as well as censoring everything from the proprietary_terms list 
  # this better than the solution given because it maintains the paragraphs

  # loop but use sub strings to step through the string so as to maintain paragraphs
  clean_string = []
  clean_string.append(negative_string)
  string_ctr = 0
  start_index = 0
  curr_start_index = 0
  negative_words_ctr = 0
  
  for word in proprietary_terms:
    negative_string = censor_phrase(word,negative_string)

  negative_string_as_list = negative_string.split()
  new_negative_string = negative_string 

  for word in negative_string_as_list:
    if curr_start_index == 0: # first word in string
      start_index  = new_negative_string.find(word)
      # if word is in negative words list , add negative counter
      if is_negative_word(word):
        negative_words_ctr+=1
      
      # this is a precaution just in case string starts with white spaces
      clean_string.append(new_negative_string[:start_index] + word)
      curr_start_index = start_index + len(word)
      # print(clean_string[-1])
    else:
      start_index  = new_negative_string[curr_start_index:].find(word)
      if negative_words_ctr < 2 and is_negative_word(word) :
        negative_words_ctr+=1
        clean_string.append(clean_string[-1] + new_negative_string[curr_start_index:curr_start_index+start_index] + word)
      elif is_negative_word(word):
        clean_string.append(clean_string[-1] + new_negative_string[curr_start_index:curr_start_index+start_index] + censor_phrase(word,word))
      else:
        clean_string.append(clean_string[-1] + new_negative_string[curr_start_index:curr_start_index+start_index] + word)
      curr_start_index+=start_index + len(word)
      # print(clean_string[-1])
  return clean_string[-1]

def censor_before_after(censored_string) :
  clean_string = []
  string_ctr = 0
  start_index = 0
  curr_start_index = 0
  censored_string_as_list=[]
  censored_string_as_list = censored_string.split()
  censored_indices=[] # will contain indices of censored words 

  def is_index_of_censor_word(index):
    for indx in censored_indices:
      if indx == index:
        return True
    return False

  # mark the indices of the strings to be censored
  for word in censored_string_as_list:
    if is_censored_word(word): 
      if string_ctr == 0 and string_ctr+1<len(censored_string_as_list):
        censored_indices.append(string_ctr+1)
      elif string_ctr+1 < len(censored_string_as_list) :
        censored_indices.append(string_ctr-1)
        censored_indices.append(string_ctr+1)
        # *** why does this not work? censored_indices + [string_ctr-1,string_ctr+1] ***
    string_ctr+=1


  string_ctr = 0 
  for word in censored_string_as_list:
    if curr_start_index == 0: # first word in string
      start_index  = censored_string.find(word)
      if is_index_of_censor_word(string_ctr):
        clean_string.append(censored_string[:start_index] + censor_word(word))
      else:
      # this is a precaution just in case string starts with white spaces
      #clean_string.append(censored_string[:start_index + len(word)])
        clean_string.append(censored_string[:start_index] + word)
      curr_start_index = start_index + len(word)
    else:
      start_index  = censored_string[curr_start_index:].find(word)
      if is_index_of_censor_word(string_ctr):
        clean_string.append(clean_string[-1] + censored_string[curr_start_index:curr_start_index+start_index] + censor_word(word))
      else:	
        clean_string.append(clean_string[-1] + censored_string[curr_start_index:curr_start_index+start_index] + word)
      curr_start_index+=start_index + len(word)
     
    string_ctr +=1
  #print (clean_string[-1])
  return clean_string[-1]
  
# Testing area
#print("Email One Before Censor of 'learning algorithms' \n")
# print(email_one)
# print(censor_phrase( 'learning algorithms',email_one))

# print("Email 2 Before Censor\n")
# print(email_two+'\n')
#print(censor_phrases_in_list(proprietary_terms,email_two))
print(censor_negative_and_proprietary_words(negative_string))
#print(censor_negative_and_proprietary_words(email_three))
print(censor_before_after(censor_negative_and_proprietary_words(negative_string)))
#print(censor_before_after(censor_negative_and_proprietary_words(email_four)))





  
