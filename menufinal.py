def mostrar_menu():
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("5. Opción 5")
    print("6. Opción 6")
    print("7. Opción 7")
    print("8. Opción 8")
    print("9. Opción 9")
    print("10. Opción 10")
    print("11. Opción 11")
    print("12. Opción 12")
    print("13. Opción 13")
    print("14. Opción 14")
    print("15. Opción 15")
    print("16. Opción 16")
    print("17. Opción 17")
    print("18. Opción 18")
    print("19. Opción 19")
    print("20. Opción 20")
    print("21. Opción 21")
    print("22. Salir")

def ejecutar_opcion(opcion):
    if opcion == 1:
        print("Ejecutando opción 1")
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)

        def main():
            try:
                num = int(input("Ingresa un número para calcular su factorial: "))
                if num < 0:
                    print("Por favor, ingresa un número entero no negativo.")
                else:
                    result = factorial(num)
                    print(f"El factorial de {num} es: {result}")
                    print("Elaborado por Leonela Vera")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")

        if __name__ == "__main__":
            main()

    elif opcion == 2:
        print("Ejecutando opción 2")
        import random
        def adivinar_numero():
            numero_a_adivinar = random.randint(1, 100)
            intentos = 10
    
            print("Bienvenido al juego de adivinar el número!")
            print("Tienes 10 intentos para adivinar un número del 1 al 100.")
    
            while intentos > 0:
                intento = int(input("Introduce un número: "))
        
                if intento < numero_a_adivinar:
                    print("El número a adivinar es mayor.")
                elif intento > numero_a_adivinar:
                    print("El número a adivinar es menor.")
                else:
                    print("¡Felicidades! ¡Has adivinado el número en", 11 - intentos, "intentos!")
                    return
        
                intentos -= 1
    
            print("Lo siento, has agotado tus intentos. El número era:", numero_a_adivinar)
            print("Elaborado por Verónica Oña")
        adivinar_numero()
        
    elif opcion == 3:
        print("Ejecutando opción 3")
        def main():
            numeros = []
            while True:
                numero = int(input("Introduce un número (introduce 0 para salir): "))
                if numero == 0:
                    break
                numeros.append(numero)
        
            if numeros:
                suma = sum(numeros)
                media = suma / len(numeros)
                print(f"La suma de los números es: {suma}")
                print(f"La media de los números es: {media}")
            else:
                print("No se ingresaron números.")

        if __name__ == "__main__":
            main()
            print("Elaborado por Daniela Castillo")
            
    elif opcion == 4:
        print("Ejecutando opción 4")
        def contar_numeros():
            cantidad = int(input("Introduce la cantidad de números a ingresar: "))
            numeros = []
            for i in range(cantidad):
                numero = float(input(f"Ingrese el número {i + 1}: "))
                numeros.append(numero)
            return numeros
        def contar_ocurrencias(numeros):
            mayores_cero = sum(1 for num in numeros if num > 0)
            menores_cero = sum(1 for num in numeros if num < 0)
            igual_cero = sum(1 for num in numeros if num == 0)

            return mayores_cero, menores_cero, igual_cero
        def imprimir_resultados(mayores_cero, menores_cero, igual_cero):
            print("Cantidad de números mayores que 0:", mayores_cero)
            print("Cantidad de números menores que 0:", menores_cero)
            print("Cantidad de números iguales a 0:", igual_cero)
            print("Elaborado por Camila Ruiz")

        def main():
            numeros = contar_numeros()
            mayores_cero, menores_cero, igual_cero = contar_ocurrencias(numeros)
            imprimir_resultados(mayores_cero, menores_cero, igual_cero)

        if __name__ == "__main__":
            main()
            
    elif opcion == 5:
        print("Ejecutando opción 5")
        def es_vocal(caracter):
            """
            Función para verificar si un carácter es una vocal.
            """
            vocales = "aeiouAEIOU"
            return caracter in vocales

        def verificar_vocal():
            """
            Función principal que solicita caracteres y verifica si son vocales o no.
            """
            while True:
                entrada = input("Introduce un caracter (o presiona Enter para salir): ")
                if entrada == '':
                    print("¡Adiós!")
                    break
                if len(entrada) == 1:
                    if es_vocal(entrada):
                        print("VOCAL")
                    else:
                        print("NO VOCAL")
                else:
                    print("Por favor, ingresa solo un caracter.")

        # Llamada a la función principal para ejecutar el programa
        if __name__ == "__main__":
            verificar_vocal()
            print("Elaborado por: Pamela Zurita")
            
    elif opcion == 6:
        print("Ejecutando opción 6")
        def obtener_numeros():
          while True:
              try:
                  num1 = int(input("Ingrese el primer número: "))
                  num2 = int(input("Ingrese el segundo número: "))
                  return num1, num2
              except ValueError:
                  print("Por favor, ingrese números enteros válidos.")

        def imprimir_pares(num1, num2):
            print(f"Números pares entre {num1} y {num2}:")
            for i in range(num1, num2 + 1):
                if i % 2 == 0:
                    print(i)

        def main():
            num1, num2 = obtener_numeros()
            imprimir_pares(num1, num2)
            print("Elaborado por Thaily Mendoza")
        
        if __name__ == "__main__":
            main()
        
    elif opcion == 7:
        print("Ejecutando opción 7")
        def imprimir_tabla_multiplicar(tabla):
            for i in range(1, 13):  
                resultado = tabla * i
                print(f"{tabla} x {i} = {resultado}")

        tabla = int(input("Ingrese la tabla: "))

        imprimir_tabla_multiplicar(tabla)

        print("Elaborado por: Angelica Torres")
        
    elif opcion == 8:
        print("Ejecutando opción 8")
        def obtener_limites():
            lim_inf = 0
            lim_sup = 0
            while lim_inf >= lim_sup:
                lim_inf = int(input("Introduce el límite inferior del intervalo: "))
                lim_sup = int(input("Introduce el límite superior del intervalo: "))
                if lim_inf >= lim_sup:
                    print("ERROR: El límite inferior debe ser menor que el superior.")
            return lim_inf, lim_sup

        def procesar_numeros(lim_inf, lim_sup):
            suma_dentro_intervalo = 0
            cont_fuera_intervalo = 0
            igual_limites = False
            num = 1
            while num != 0:
                num = int(input("Introduce un número (0 para salir): "))
                if num > lim_inf and num < lim_sup:
                    suma_dentro_intervalo += num
                else:
                    cont_fuera_intervalo += 1
                if num == lim_inf or num == lim_sup:
                    igual_limites = True
            return suma_dentro_intervalo, cont_fuera_intervalo, igual_limites

        def main():
            lim_inf, lim_sup = obtener_limites()
            suma_dentro_intervalo, cont_fuera_intervalo, igual_limites = procesar_numeros(lim_inf, lim_sup)
            print("La suma de los números dentro del intervalo es", suma_dentro_intervalo)
            print("La cantidad de números fuera del intervalo es", cont_fuera_intervalo)
            if igual_limites:
                print("Se ha introducido algún número igual a los límites del intervalo.")
            else:
                print("No se ha introducido ningún número igual a los límites del intervalo.")

        if __name__ == "__main__":
            main()
        print("Elaborado por: Luisa Paladines")
        
    elif opcion == 9:
        print("Ejecutando opción 9")
        def obtener_datos_potencia():
            base=float(input("Ingrese la base de la potencia: "))
            exponente=-1

            while exponente < 0:
                exponente = int(input("Ingrese el exponente de la potencia: "))
                if exponente < 0:
                    print("ERROR: El exponente debe ser positivo")
            return base, exponente

        def calcular_potencia(base, exponente):
                potencia = 1
                for _ in range(exponente):
                    potencia *= base
                return potencia
        def main():
            base, exponente = obtener_datos_potencia()
            resultado_potencia = calcular_potencia(base, exponente)
            print(f"La potencia de {base} elevado a {exponente} es: {resultado_potencia}")

        if __name__ == "__main__":
            main()
        print("Elaborado por: Jeraldy Tumipamba")
        
    elif opcion == 10:
        print("Ejecutando opción 10")
        print ("Las tablas del 1 al 5")
        def tablas ():
            a = int(input("Ingrese un número del 1 al 5 para saber su tabla: "))
            for i in range (1, 11, 1):
                b = a * i
                print (a, " * ", i,  " = ", b)
        tablas ()
        print ("Elaborado por: Bacuy David")
        
    elif opcion == 11:
        print("Ejecutando opción 11")
        n=-1
        while n<0:
            n = int(input("Ingresa un número:"))
        if n>0:
            switch = 0
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                switch = 1
                break
        if switch!=1:
            print("Es un número primo")
        else:
            print("No es un número primo")
        print("Elaborado por Navarrete Maykel")
        
    elif opcion == 12:
        print("Ejecutando opción 12")
        def calcular_ahorros():
            ahorros_totales = 0
            for mes in range(1, 13):
                deposito = int(input("Ingrese la cantidad depositada para el mes " + str(mes) + ": "))
                ahorros_totales += deposito
                print("Llevas ahorrado un total de: " + str(ahorros_totales))
            print("Al final del año, habrás ahorrado un total de: " + str(ahorros_totales))
        def main():
            calcular_ahorros()
        if __name__ == "__main__":
            main()
            print("Elaborado por Leonardo Cunalata")
        
    elif opcion == 13:
        print("Ejecutando opción 13")
def ingresar_horas_trabajadas(dias):
    horas_trabajadas = []
    for i in range(dias):
        horas = float(input(f"Ingrese las horas trabajadas el día {i+1}: "))
        horas_trabajadas.append(horas)
    return horas_trabajadas

def calcular_total_horas(horas_trabajadas):
    return sum(horas_trabajadas)

def calcular_sueldo(total_horas, salario_por_hora):
    return total_horas * salario_por_hora

def main():
    dias_trabajados = 6
    horas_trabajadas = ingresar_horas_trabajadas(dias_trabajados)
    salario_por_hora = 10  # Ejemplo: $10 por hora
    total_horas_trabajadas = calcular_total_horas(horas_trabajadas)
    sueldo = calcular_sueldo(total_horas_trabajadas, salario_por_hora)
    print(f"Total de horas trabajadas durante la semana: {total_horas_trabajadas}")
    print(f"Sueldo correspondiente: ${sueldo}")

if __name__ == "__main__":
    main()
    print("Elaborado por Valeria Manobanda")         
    elif opcion == 14:
        print("Ejecutando opción 14")
def calcular_punto_encuentro(km1, km2):
    distancia_entre_personas = abs(km1 - km2)
    return max(km1, km2) - distancia_entre_personas / 2
def main():
    # Posiciones iniciales de las personas en la carretera
    km_persona1 = 70
    km_persona2 = 150
    punto_encuentro = calcular_punto_encuentro(km_persona1, km_persona2)
    print(f"Las personas se encontrarán en el kilómetro {punto_encuentro}.")
if __name__ == "__main__":
    main()
    print("Elaborado por Gabriel Gusqui")  
    elif opcion == 15:
        print("Ejecutando opción 15")
        def calcular_pago_mensual(meses):
    pago_mensual = 0
    for mes in range(meses):
        pago_mensual += 10 * (2 ** mes)
    return pago_mensual

def calcular_total_pagado(meses):
    total_pagado = 0
    for mes in range(meses):
        total_pagado += 10 * (2 ** mes)
    return total_pagado

def main():
    meses = 20

    pago_mensual = calcular_pago_mensual(meses)
    total_pagado = calcular_total_pagado(meses)

    print(f"El pago mensual es de {pago_mensual} €.")
    print(f"El total pagado después de {meses} meses es de {total_pagado} €.")

if __name__ == "__main__":
    main()
print("Elaborado por Gabriel Gusqui")
            
    elif opcion == 16:
        print("Ejecutando opción 16")
        def calcular_sueldo(horas, tarifa):
            return horas * tarifa

        def main():
            n = int(input("Número de empleados: "))
            total_pago = 0

            for i in range(1, n + 1):
                horas = float(input(f"Horas trabajadas por empleado {i}: "))
                tarifa = float(input(f"Tarifa por hora para empleado {i}: "))
        
                sueldo = calcular_sueldo(horas, tarifa)
                total_pago += sueldo

                print(f"Sueldo de empleado {i}: ${sueldo}")

            print(f"\nPago total de la empresa por {n} empleados: ${total_pago}")

        main()

        print("Elaborado por Juan Toapanta")
        
    elif opcion == 17:
        print("Ejecutando opción 17")
        def calcular_sueldo_semanal(horas_trabajadas, tarifa_por_hora):
           return horas_trabajadas * tarifa_por_hora
        n = int(input("Ingrese el número de empleados: "))
        sueldo_total = 0
        for i in range(n):
            horas_trabajadas = float(input(f"Ingrese las horas trabajadas para el empleado {i+1}: "))
            tarifa_por_hora = float(input(f"Ingrese la tarifa por hora para el empleado {i+1}: "))
            sueldo_semanal = calcular_sueldo_semanal(horas_trabajadas, tarifa_por_hora)
            sueldo_total += sueldo_semanal
            print(f"El sueldo semanal del empleado {i+1} es ${sueldo_semanal}")
        print(f"\nLa empresa pagó un total de ${sueldo_total} a {n} empleados.")
        print("Elaborado por: Alessia Moreno")
        
    elif opcion == 18:
        print("Ejecutando opción 18")
        import time
        def cronometro():
            segundos=0
            minutos=0
            horas = 0
            while True:
                print(f"{horas:02d}:{minutos:02d}:{segundos:02d}", end="\r")
                time.sleep(1)
                segundos= segundos+1
                if segundos == 60:
                    segundos=0
                    minutos=minutos+ 1
                if minutos == 60:
                    minutos=0
                    horas= horas+1
        try:
            cronometro()
        except KeyboardInterrupt:
            print("\nCronómetro detenido.")
            print("Elaborado por: Katty Puco")
            
    elif opcion == 19:
        print("Ejecutando opción 19")
        def clear_screen():
            print("\n" * 50)

        def display_menu():
            print("Menú:")
            print("a. Opción A")
            print("b. Opción B")
            print("c. Opción C")
            print("d. Opción D")
            print("e. Opción E")
            print("e. Salir")   

        def process_option(option):
            if option.lower() == 'a':
                print("Ha seleccionado la Opción A")
            elif option.lower() == 'b':
                print("Ha seleccionado la Opción B")
            elif option.lower() == 'c':
                print("Ha seleccionado la Opción C")
            elif option.lower() == 'd':
                print("Ha seleccionado la Opción D")
            elif option.lower() == 'e':
                print("Ha seleccionado la Opción E")
            elif option.lower() == 'e':   
                print("Saliendo del programa...")
            else:
                print("Opción no válida. Inténtelo de nuevo.")

        def main():
            opcion = ''

            while opcion.lower() != 'e':   
                clear_screen()
                display_menu()
                opcion = input("Seleccione una opción: ")
                process_option(opcion)

        if __name__ == "__main__":
            main()
            print("Elaborado por Samuel Monte")
            
    elif opcion == 20:
        print("Ejecutando opción 20")
        def es_primo(num):
            if num <= 1:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        def mostrar_primos(cantidad):
            primos_encontrados = 0
            numero = 2
            while primos_encontrados < cantidad:
                if es_primo(numero):
                    print(numero, end=" ")
                    primos_encontrados += 1
                numero += 1

        try:
            cantidad = int(input("Ingrese la cantidad de números primos que desea mostrar: "))
            if cantidad <= 0:
                print("Por favor, ingrese un número entero positivo.")
            else:
                print(f"Los primeros {cantidad} números primos son:")
                mostrar_primos(cantidad)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
        print("Elaborado por Jade Argotty")
        
    elif opcion == 21:
        print("Ejecutando opción 21")
        def suma(a, b):
            return a + b

        def resta(a, b):
            return a - b

        def multiplicacion(a, b):
            return a * b

        def division(a, b):
            if b == 0:
                return "No se puede dividir por cero."
            else:
                return a / b

        def main():
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            print("Suma:", suma(num1, num2))
            print("Resta:", resta(num1, num2))
            print("Multiplicación:", multiplicacion(num1, num2))
            print("División:", division(num1, num2))
            print("Elaborado por: Verónica Oña")

        if __name__ == "__main__":
            main()

    elif opcion == 22:
        print("Saliendo del programa...")
        exit()
    else:
        print("Opción no válida")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Selecciona una opción: "))
        ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()
