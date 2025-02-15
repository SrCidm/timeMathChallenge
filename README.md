🧮 Math Game
Welcome to Math Game, an exciting math game designed to test your arithmetic skills while having fun. Solve math problems with different operators (+, -, *, /) at customized difficulty levels. Show off your numerical skills and improve your response times!

🚀 Main Features
Customized Difficulties: Choose from three difficulty levels:
Easy (2 problems)
Medium (5 problems)
Hard (10 problems)
Math Operations: Practice addition, subtraction, multiplication, and division.
Divisions always have integer results to avoid confusion.
Unlimited Retries: If you make a mistake, you can try as many times as needed until you get it right.
Precise Timing: Measure how long it takes to complete all problems and calculate the average time per problem.
Accuracy Percentage: Get a detailed summary of your performance, including the percentage of correct answers.
Motivational Messages: Receive positive feedback based on your performance. There's always room for improvement!
Play Again: After each game, you have the option to play again without restarting the program.

📋 Requirements
To run this game, you need to have Python 3.x installed on your system. Make sure your environment is set up correctly.

🎮 How to Play
1. Clone the Repository:
```bash
git clone https://github.com/your-username/math-game.git
cd math-game
```
2. Run the Game:
```bash
python math_game.py
```
3. Select the Difficulty:
Enter 1 for easy level (2 problems).
Enter 2 for medium level (5 problems).
Enter 3 for hard level (10 problems).
4. Solve the Problems:
Answer each problem by entering the correct result.
If you make a mistake, you will have the opportunity to try again.
5. Check Your Results:
At the end, you will get a summary with:
Number of problems solved correctly.
Total time taken.
Average time per problem.
Accuracy percentage.
Motivational messages based on your performance.
6. Play Again:
If you want to play another game, simply respond "yes", "y", "si", "s" or "yeah" when asked.

📊 Example Game
```plaintext
Welcome to the Math Game!
Select difficulty level:
1. Easy (2 problems)
2. Medium (5 problems)
3. Hard (10 problems)
Enter your choice (1/2/3): 2
You will have to solve 5 problems. Let's begin!

Press Enter to start...
--------------------

Problem 1: 7 + 9 = 16
Correct!

Problem 2: 12 / 4 = 3.0
Correct!

Problem 3: 11 - 4 = 6
Incorrect. Try again.

Problem 3: 11 - 4 = 7.0
Correct!

Problem 4: 3 * 12 = 36
Correct!

Problem 5: 8 + 5 = 14
Correct!

Game over! You solved 5 out of 5 problems correctly.
Total time: 35.42 seconds
Average time per problem: 7.08 seconds
Your accuracy: 83.33%
Total wrong attempts: 1
--------------------

Great job! You're a math wizard!
Do you want to play again? (yes/no): yes
```

🛠️ Code Structure
The code is divided into modular functions for ease of understanding and maintenance:

`generate_problem()`: Generates a random math problem using defined operands and operators. Ensures divisions have integer results.
`select_difficulty()`: Allows the user to select the game's difficulty.
`main()`: Controls the main game flow, including timing, answer counting, and statistics calculation.

📝 License
This project is under the MIT license. You can freely use, modify, and distribute this code as long as the original attribution is maintained.