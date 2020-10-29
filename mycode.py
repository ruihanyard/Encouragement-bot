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
      encouragement_list.append("that tomorrow will be a better day")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling")
      counter -= 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("that you are stronger than you think")
      counter += 1
    if each_word == "worried":
      feelings_list.append("worried")
      encouragement_list.append("to take a deep breath")
      counter += 1
    if each_word == "fine":
      feelings_list.append("fine")
      encouragement_list.append("to stay this way and be positive")
      counter -= 1
    if each_word == "disappointed":
      feelings_list.append("disappointed")
      encouragement_list.append("to cheer up as your down times will pass")
      counter += 1
    if each_word == "scared:
      feelings_list.append("scared")
      encouragement_list.append("there's nothing to be afraid of")
      counter += 1
    if each_word == "lonely":
      feelings_list.append("lonely")
      encouragement_list.append("that you're not alone in this tough journey of life")
      counter += 1
      
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "" + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "" + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
