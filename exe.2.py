produtos=float(input("Digite quantos produtos foram: "))
cor=(input("Digite a cor do selo: "))
if cor=="verde":
    print("O preço é de",5.50*produtos , "Reais.")
elif cor=="azul":
    print("O preço é de",5.70*produtos , "Reais.")
elif cor=="branco":
    print("O preço é de",4.00*produtos , "Reais.")
elif cor=="rosa":
    print("O preço é de",3.50*produtos , "Reais.")
else:
    print("Digite uma cor válida.")