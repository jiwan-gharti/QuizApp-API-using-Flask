
# QuizApp API
## Installation
Just follow this steps to run locally

Clone this project in your directory

```bash
git clone https://github.com/jiwan-gharti/quizapp-api-using-flask.git
```
    
Go to "quiz-app-api-flask" folder
```bash
cd quizapp-api-using-flask
```

Create Virtual Environment
```bash
python3 -m venv venv
```

Activate Virtual Environment
```bash
source venv/bin/activate
```

Install neccessary libraries and packages
```bash
pip install -r requirements.txt
```

Run main.py file
```bash
python app.py
```
Development server will start at http://127.0.0.1:5000/

## API Reference

#### 1. SignUp User/Admin

```http
  POST /user
```
Users will be signed up for using the application. Users will be Admin or Normal
Users.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. Email of User |
| `username` | `string` | **Required**. Username of User |
| `password` | `string` | **Required**. Password of User |
| `is_admin` | `integer` | **Required**. Admin status: 0 not admin, 1 admin |

SAMPLE JSON REQUEST FORMAT
```Json Format
{
    "name":"nawij itrahg",
    "username":"nawij itrahg",
    "password":"123",
    "is_admin":1
}

#### 2. Login

```http
  POST /api/auth
```
User can be able to login using the credentials. In this session_id will be created
which will be further used for all subsequent activities.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email`      | `string` | **Required**. Username created at signup |
| `password` | `string` | **Required**. Password created at signup |


SAMPLE JSON REQUEST FORMAT
```Json Format
{
    "username":"sak",
    "password":"123"
}
```
SAMPLE JSON RESPONSE FORMAT

Success
```Json Format
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoxLCJleHAiOjE2ODE0MDIzODl9.FccYuNhGx7OqL4KPmTYR65zvngGXnrwmTCZVZd978gs"
}
```

Error
```Json Format
{"message": "Incorrect Username or Password"}
```
#### 3. Add Category

```http
  POST /api/category
```
 Admin can add new questions in the questions table.


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `category`| `string` | **Required**. category statement |

```Json Format
{
    "category":"Networking"
}
```
and perform CRUD operation only by admin


#### 4. Add Question Type
```http
  POST /api/question_type
```
 Admin can add new questions in the questions table.


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `question_type`| `string` | **Required**. category statement |

```Json Format
{
    "question_type":"hard"
}
```
and perform CRUD operation only by admin

#### 5. Add Quiz Type

```http
  POST /api/quiz_type
```
 Admin can add new quiz_type in the quiz_type table.


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `question_type`| `string` | **Required**. category statement |

```Json Format
{
    "quiz_type":"ML"
}
```
and perform CRUD operation only by admin


#### 6. Add Quiz

for the card like feature

```http
  POST /api/quiz
```
 Admin can add new quiz in the quiz table.

SAMPLE JSON REQUEST FORMAT
```Json Format
{
    "title":"Science Easy test",
    "quiz_type_id":"1",
    "user_id": "1",
    "categories_id":["1","2"]
    
}
```

#### 7. Add Question
```http
  POST /quiz
```
 Admin can add new questions in the quiz_question table.



SAMPLE JSON REQUEST FORMAT
```Json Format
{
    "question": "Question 1",
    "choice1": "choice 1",
    "choice2": "choice 2",
    "choice3": "choice 3",
    "choice4": "choice 4",
    "correct_answer": "3",
    "published": 0,
    "quiz_id": "1",
    "question_type_id": "3",
}
```



#### 8. List All Questions(By Admin)

```http
  GET /api/question
```
Admin can list all questions persisted in the database

SAMPLE JSON RESPONSE FORMAT

Success
```Json Format
[
    {
        "correct_answer": 4,
        "choice1": "20",
        "choice2": "21",
        "choice3": "22",
        "choice4": "23",
        "question": "What is a+b if a = 4 and b = 19?",
        "question_id": 1,
        "quiz_id": 1,
        "question_type_id": "3",
        "published": true,
    },
    {
        "correct_answer": 2,
        "choice1": "3",
        "choice2": "4",
        "choice3": "5",
        "choice4": "6",
        "question": "If x = 9 and y = 5, that what is x-y?",
        "question_id": 2,
        "question_type_id": "1",
        "published": false,
    }
]
```

Error
```Json Format
{"message": "Don\'t have required privileges"}
```



#### 9. List All Questions(By User)

```http
  GET /api/quiz_test/<quiz_id>
```
Admin can list all questions persisted in the database

SAMPLE JSON RESPONSE FORMAT

Success
```Json Format
[
    {
        "correct_answer": 4,
        "choice1": "20",
        "choice2": "21",
        "choice3": "22",
        "choice4": "23",
        "question": "What is a+b if a = 4 and b = 19?",
        "question_id": 1,
        "quiz_id": 1,
        "question_type_id": "3",
        "published": true,
    },
    {
        "correct_answer": 2,
        "choice1": "3",
        "choice2": "4",
        "choice3": "5",
        "choice4": "6",
        "question": "If x = 9 and y = 5, that what is x-y?",
        "question_id": 2,
        "question_type_id": "1",
        "published": false,
    }
]
```


#### 10. See Already Completed quizes' results
```http
  POST /api/quiz_results
```

#### 11. See onging quiz Completed quizes' results
```http
  POST /api/quiz_test/<quiz_id>
```

Request Json Format
```Json Format
[
    {
      "question_id":"1",
      "answer":"3"
    },
    {
      "question_id":"1",
      "answer":"3"
    },
    {
      "question_id":"1",
      "answer":"3"
    }
]
```


Response Json Format
```Json Format
{
    "is_submitted": "1",
    "score_achived": "3",
    "is_active": "0",
    "quiz": {
        "id": "1",
        "title": "hello Easy test"
    },
    "id": "1",
    "user_id": "1"
}
```






