import secrets 
import string

N = 8
res = ''.join(random.choices(string.ascii_letters, k=N))
print("The generated random password is: "+ str(res))
