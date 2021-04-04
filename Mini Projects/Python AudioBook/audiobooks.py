import pyttsx3, PyPDF2

book=open("The art of public speaking.pdf", "rb") #Extracting the book
reader = PyPDF2.PdfFileReader(book)  
pages = reader.numPages  #Getting number of pages in the book
narrator=pyttsx3.init()  #Inititating text to speech mechanism 

for i in range(9, pages):        #Loop to read all the pages
    content = reader.getPage(i)   #Getting content of the page
    text=content.extractText()    #Extracting text from the page
    narrator.say(text)            #Narrator speaking the content of the page.  
    narrator.runAndWait()