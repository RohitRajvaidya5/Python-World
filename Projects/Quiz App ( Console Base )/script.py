import json

# Load questions from the JSON file
try:

    with open('question.json', 'r') as questions:
        data = json.load(questions)

except FileNotFoundError:

    print("Question file not found.")

    exit()

except json.JSONDecodeError:
    
    print("JSON format is incorrect")

    exit()

count = 0

# Loop through each question
for i in range(len(data)):

    try:
        print(data[i]['question'])

        # Print each option on a new line
        for option in data[i]['options']:
            print(option)

        # Take user input
        ans = input("Enter the correct option: ").upper()

        # Check answer
        if ans == data[i]['answer']:
            print("Correct answer, let's go for the next!\n")
            count = count + 1
        else:
            print(f"Incorrect answer, one point taken.\nCorrect Answer is '{data[i]['answer']}' ")
            if count == 0:
                count = 0
            else:
                count = count - 1
            
    except KeyError as e:
        print(f"Missing key in question data {e}")
        continue

    except Exception as e:
        print(f"Unexpected Error : {e}")
        continue

# Final score
print(f"Total Score: {count}")
