import json

# Load questions from the JSON file
with open('question.json', 'r') as questions:
    data = json.load(questions)

count = 0

# Loop through each question
for i in range(len(data)):
    print(data[i]['question'])

    # Print each option on a new line
    for option in data[i]['options']:
        print(option)

    # Take user input
    ans = input("Enter the correct option: ")

    # Check answer
    if ans == data[i]['answer']:
        print("Correct answer, let's go for the next!\n")
        count = count + 1
    else:
        print("Incorrect answer, one point taken.\n")
        count = count - 1

# Final score
print(f"Total Score: {count}")
