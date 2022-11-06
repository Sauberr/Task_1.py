 def swap_case(s):
     b = ''
     for i in s:
         if i.isupper():
             b += i.lower()
         else:
             b += i.upper()
     return b

 print(swap_case('HackerRank.com presents "Pythonist 2".'))
 
 s = 'this is a string'
 b = s.split()
 print('-'.join(b))
