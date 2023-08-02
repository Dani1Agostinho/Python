



ma = None
me = None
for i in range(1,3):
   x = float(input("Digite um número: "))
   ma = ma if ma != None and ma >  x else x
   me = me if me != None and me < x else x

print ('O maior valor digitado foi {} e o menor foi {}'.format(ma,me))