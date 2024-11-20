import random
questions = {
    "python": [
        {"question":"What is the output of print(2 ** 3)?", "answer":"8"},
        {"question":"Which keyword is used to define a function?", "answer": "def"},
        {"question":"What is the built-in data type for a sequence of characters?","answer": "str"},
        {"question":"Which module is used for regular expressions?","answer": "re"},
        {"question":"What does 'len()' function do?", "answer":"returns length"},
        {"question":"Which keyword is used to handle exceptions?", "answer":"try"},
        {"question":"What is the correct file extension for Python files?", "answer":".py"},
        {"question":"What is the output of list(range(5))?", "answer":"[0, 1, 2, 3, 4]"},
        {"question":"How do you create a dictionary in Python?", "answer":"{}"},
    ],
    "java":[
        {"question":"What is the output of print(2 ** 3)?", "answer":"8"},
        {"question":"Which of these is the correct way to declare a variable in Java?","answer":"int num = 10;"},
        {"question":"Which of the following methods is used to start a thread in Java?","answer":"start()"},
        {"question":"What is the size of a float variable in Java?","answer": "32 bits"},
        {"question":"Which of the following is not a valid Java keyword?","answer":"string"},
        {"question":"Which of the following is the parent class of every class in Java?","answer":"Object"},
        {"question":"What is the default value of an int variable in Java?","answer": "0"},
        {"question":"Which of the following is the correct syntax to print 'Hello World' in Java?","answer":"System.out.println('Hello World');"},
        {"question":"Which of the following is a valid Java keyword?","answer": "void"},
        {"question":"Which method is used to get the length of a string in Java?","answer":"length()"},
        {"question":"Which of these is not a valid access modifier in Java?","answer": "unprotected"},
        {"question":"Which class is the superclass of all classes in Java?","answer":  "Object"},
    ],
     "dbms":[
        {"question":"What is the output of print(2 ** 3)?", "answer":"8"},
        {"question":"What does DBMS stand for?","answer": "Database Management System"},
        {"question":"What is a primary key?","answer": "Unique identifier"},
        {"question":"What is the purpose of normalization?","answer": "Eliminate redundancy"},
        {"question":"What SQL command is used to retrieve data?","answer": "SELECT"},
        {"question":"What is a foreign key?","answer": "Reference to another table"},
        {"question":"What is the purpose of an index?","answer": "Speed up retrieval"},
        {"question":"What is the ACID property?","answer": "Atomicity, Consistency, Isolation, Durability"},
        {"question":"What does SQL stand for?", "answer":"Structured Query Language"},
        {"question":"What is a join in SQL?","answer": "Combining tables"},
        {"question":"What is the use of 'GROUP BY' clause?", "answer":"Aggregate data"}
    ]
}
users = {}
def register():
    print("Register a new account :")
    username = (input("Enter a username :"))
    if username in users:
        print("Username already exists. Please log in or choose a different username")
        return False
    password = input("Enter a unique password :")
    users[username] = password
    print("Registration successful.")
    return True
def login() :
    print("Login to your account :")
    username = input("Enter your username :")
    password = input("Enter your privacy password :")
    if users.get(username) == password:
        print("Login Successful.")
        return True
    else :
        print("Invalid username or password.")
        return False

def start_quiz():
    print("Choose a Language : python, java , dbms")
    language_choice = input("Enter language :").lower()

    if language_choice in questions :
       score = 0
       selected_questions = random.sample(questions[language_choice], len(questions[language_choice]))

       for q in selected_questions:
          user_answer = input(q["question"] + " ")
          if user_answer.strip().lower() == q["answer"].lower():
              print("correct!")
              score +=1
          else:
              print("Wrong Answer!",)
       print(f"Quiz finished! Your score : {score}/{len(selected_questions)}")
    else :
        print("Language Not Supported.")

print("Welcome to the Quiz Application")
while True :
    print("\n1.Register\n2.Login\n3.Exit")
    choice = input("Enter your choice :")

    if choice =="1":
        if register():
            start_quiz()
    elif choice =="2":
        if login():
            start_quiz()
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Invalid choice. Please try again.")    