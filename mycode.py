print("Title of program: Encouragement bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("Tomorrow will be a better day!")
      counter += 1
      
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("Keep smiling!")
      counter += 1
      
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("You are stronger than you think!")
      counter += 1
      
   if each_word == "anxious":
      feelings_list.append("anxious")
      encouragement_list.append("take a deep breath")
      counter += 1
      
   if each_word == "stressed":
      feelings_list.append("stressed")
      encouragement_list.append("take a deep breath")
      counter += 1
      
   if each_word == "frustrated":
      feelings_list.append("frustrated")
      encouragement_list.append("take a deep breath and calm your mind")
      counter += 1
      
   if each_word == "disappointed":
      feelings_list.append("disappointed")
      encouragement_list.append("You are amazing, keep on fighting!")
      counter += 1
      
   if each_word == "embarrassed":
      feelings_list.append("embarrassed")
      encouragement_list.append("Nothing about you is shameful, you are AMAZING!")
      counter += 1
      
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
