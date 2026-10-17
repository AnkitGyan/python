#built in methods
st = "I Like Python"
print(st)
del st   #to deleter full string

st = 'I Like Python'
stnew = st.capitalize()
print(stnew)

stnew2 = st.casefold()
print(stnew2)

st2 = 'i like what you like'
n = st2.count('i')
print(n)

n2 = st2.count('like')
print(n2)

st3 = 'abes.ac.in'
print(st3.startswith('abes'))
print(st3.endswith('in'))

n = st2.find('like')
print(n)

st4 = 'I like Python'
stnew3 = st4.lower()
stnew4 = st4.upper()
print(stnew3)
print(stnew4)
st5 = st4.swapcase()
print(st5)

stnew5 = st.title()
print(stnew5)

stnew7 = st4.replace('Python','java')
print(stnew7) 
