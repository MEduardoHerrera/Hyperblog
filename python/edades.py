def calcular_edad_abel(edad_total, diferencia_edad):
    edad_abel = (edad_total - diferencia_edad) / 2
    return edad_abel

edad_total = 36
diferencia_edad = 8

edad_abel = calcular_edad_abel(edad_total, diferencia_edad)

print("Abel tiene", edad_abel, "años.")

# Cuando nació Abel, María tenía 8 años. Si actualmente sus edades suman 36 años. 
# ¿Cuántos años tiene Abel?