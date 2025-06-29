from datetime import datetime
entrada = input("Digite a hora no formato hh:mm: ")
hora = datetime.strptime(entrada, "%H:%M")
if hora.hour >= 00 and hora.hour <= 11:
    print("BOM DIA!")
elif hora.hour >11 and hora.hour <= 17:
    print("BOA TARDE!")
elif hora.hour >17 and hora.hour <= 23:
    print("BOA NOITE!")        