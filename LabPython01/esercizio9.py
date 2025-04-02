s='Apelle, figlio di Apollo Fece una palla di pelle di pollo Tutti i pesci vennero a galla Per vedere la palla di pelle di pollo Fatta da Apelle figlio di Apollo.'
s1=' Apelle, figlio di Apollo \n Fece una palla di pelle di pollo \n Tutti i pesci vennero a galla \n Per vedere la palla di pelle di pollo \n Fatta da Apelle figlio di Apollo.'
print(s1)
print(len(s1))
print(s1.count('ll'))
s2=s1.replace(',', '')
s3=(s2.replace('\n',''))
print(s3)
a=s1.upper()
a=a.count('A')
print(a)