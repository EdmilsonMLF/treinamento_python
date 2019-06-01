"""
idade = int(input("digite a idade "))
if idade >= 16 :
    print("pode votar")
else:
    print("não pode votar")
"""
idade2 = int(input("digite a idade2 "))
if idade2 < 16 :
    print("não pode votar")
elif idade2 >= 16 and idade2 < 18:
    print("pode votar (não é obrigatório)")
elif idade2 > 18 and idade2 < 70:
    print("pode votar (é obrigado)")
else:
     print("pode votar (não é obrigatório)")