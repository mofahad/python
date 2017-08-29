#PROGRAM TO WRITE INTO A FILE

text = "SAMPLE FOR A TESTING \n NEW LINE"
SaveFile = open("exampleFile.txt","w")
SaveFile.write(text)
SaveFile.close

