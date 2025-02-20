print ("Vamos calcular o orçamento da revisão e formatação do seu trabalho")
caracteres= int (input
 ("Qual a quantidade de caracteres com espaço em seu trabalho? - verificar nas propriedades do documento Word "))
laudas = (caracteres/1400)
print (laudas)
prazo = int (input ("Coloque o prazo desejado. 1 - normal, 2 - urgente, 3- expresso"))
if laudas <=15:
  if prazo==1:
    valor=laudas*8
  elif prazo==2:
    valor=laudas*11
  elif prazo==3:
    valor= laudas*22
else:
  if prazo==1:
    valor=laudas*6
  elif prazo==2:
    valor=laudas*8
  elif prazo==3:
    valor=laudas*11

print ("O orçamento para este serviço é de R$", round (valor,2) , " e será devolvido formatado e revisado no prazo", prazo)
