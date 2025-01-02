def unpass(dic,text):
     og_text=""
     for ch in text:
         if ch in dic :
             og_text +=dic[ch]
         else:
             og_text += ch
     return og_text

dic_pass={
      'a': 'h',
      'b':'e',
      'c':'l',
      'd':'o',
      'e':'y',
      'f':'o',
      'g':'u'
  }


pass_text="abcdefg"
print("main text :",unpass(dic_pass,pass_text))




