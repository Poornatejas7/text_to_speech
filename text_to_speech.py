# ----- Text to Speech ------- #


'''from gtts import gTTS
from PyPDF2 import PdfReader
import os

f  =open('startup idea 1.pdf','rb')
pdf = PdfReader(f)
text = ''
for pages in pdf.pages:
  text += pages.extract_text()

language = 'en'

audio = gTTS(text=text, lang=language,slow=False)
audio.save('audio.wav')
os.system('audio.wav')'''

my_list = [x if x % 2 == 0 else -x for x in range(10)]
print(my_list) 
my_list = [x for x in range(10) if x % 2 == 0 else -x]
