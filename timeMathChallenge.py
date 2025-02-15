import random
import time

# Constantes
OPERATORS = ['+', '-', '*', '/']
MIN_OPERAND = 3
MAX_OPERAND = 12

def generate_problem():
    """
    Genera un problema matemático aleatorio y devuelve la expresión y la respuesta.
    Asegura que las divisiones tengan resultados enteros.
    """
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    
    # Si el operador es '/', asegurarse de que el resultado sea entero
    operator = random.choice(OPERATORS)
    if operator == '/':
        # Intercambiar left y right para que left sea divisible por right
        left, right = right * random.randint(1, MAX_OPERAND // right), right
    
    expr = f'{left} {operator} {right}'
    answer = eval(expr)  # Calcula la respuesta usando eval (seguro en este contexto)
    return expr, answer

def select_difficulty():
    """
    Permite al usuario seleccionar la dificultad del juego.
    Devuelve el número de problemas correspondiente a la dificultad seleccionada.
    """
    print("Select difficulty level:")
    print("1. Easy (2 problems)")
    print("2. Medium (5 problems)")
    print("3. Hard (10 problems)")
    
    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice in ['1', '2', '3']:
            return [2, 5, 10][int(choice) - 1]  # Fácil: 2, Medio: 5, Difícil: 10
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def main():
    print("Welcome to the Math Game!")
    TOTAL_PROBLEMS = select_difficulty()  # Seleccionar la dificultad
    print(f"You will have to solve {TOTAL_PROBLEMS} problems. Let's begin!\n")
    input("Press Enter to start...")
    print("--------------------\n")
    
    start_time = time.time()  # Guardar el tiempo de inicio
    
    correct_answers = 0
    wrong_attempts = 0  # Contador de intentos incorrectos
    
    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem()
        
        while True:
            try:
                # Mostrar el problema y pedir la respuesta
                guess = input(f"Problem {i + 1}: {expr} = ")
                
                # Validar que la entrada sea un número (entero o decimal)
                guess = float(guess)  # Permitir respuestas decimales
                
                # Verificar si la respuesta es correcta
                if guess == answer:
                    print("Correct!\n")
                    correct_answers += 1
                    break  # Pasa al siguiente problema
                else:
                    print(f"Incorrect. Try again.\n")
                    wrong_attempts += 1  # Incrementa el contador de intentos fallidos
            except ValueError:
                print("Invalid input. Please enter a number.\n")
    
    end_time = time.time()
    total_time = end_time - start_time
    
    # Calcular el porcentaje de aciertos
    total_attempts = TOTAL_PROBLEMS + wrong_attempts  # Total de intentos incluyendo fallos
    if total_attempts > 0:  # Evitar división por cero
        percentage_correct = (correct_answers / total_attempts) * 100
    else:
        percentage_correct = 0
        print("No attempts were made. Accuracy cannot be calculated.")
    
    # Mostrar el resultado final con el porcentaje de aciertos
    print(f"Game over! You solved {correct_answers} out of {TOTAL_PROBLEMS} problems correctly.")
    print(f"Total time: {total_time:.2f} seconds")
    average_time_per_problem = total_time / TOTAL_PROBLEMS if TOTAL_PROBLEMS > 0 else 0
    print(f"Average time per problem: {average_time_per_problem:.2f} seconds")
    print(f"Your accuracy: {percentage_correct:.2f}%")  # Muestra el porcentaje con dos decimales
    print(f"Total wrong attempts: {wrong_attempts}")
    print("--------------------\n")
    
    # Mensaje motivacional
    if percentage_correct >= 80:
        print("Great job! You're a math wizard!")
    elif percentage_correct >= 50:
        print("Not bad! Keep practicing and you'll get better!")
    else:
        print("Better luck next time! Practice makes perfect!")
    
    # Opción para jugar nuevamente
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again in ['yes', 'y', 'si', 's', 'yeah']:
        main()

if __name__ == "__main__":
    main()