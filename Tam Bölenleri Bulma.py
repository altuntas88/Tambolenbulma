
# coding: utf-8

# In[ ]:


def tambolenleribulma(sayi):
  tam_bolenler=[]
  
  for i in range(2,sayi):
    if(sayi%i==0):
      tam_bolenler.append(i)
  return tam_bolenler
  
while True:
  sayi=input("Sayı Giriniz")
  if(sayi=="q"):
    print("Programdan Çıkılıyor")
    break
  else:
    sayi=int(sayi)
    print(tambolenleribulma(sayi))

