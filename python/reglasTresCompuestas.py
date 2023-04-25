def carpinteros_dias(carpinteros1, horas1, sillas1, dias1, carpinteros2, horas2, sillas2):
    sillas_por_carpintero1 = sillas1 / (carpinteros1 * horas1 * dias1)
    dias2 = sillas2 / (carpinteros2 * horas2 * sillas_por_carpintero1)
    return dias2
print(carpinteros_dias(40, 8, 320, 10, 55, 4, 440))

"""
Ahora para este Un grupo de 40 carpinteros trabaja 8 horas diarias y construye 320 sillas en 10 días. 
¿En cuántos días harán 440 sillas 55 carpinteros que trabajan 4 horas diarias?
"""