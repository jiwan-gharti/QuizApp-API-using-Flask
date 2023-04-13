from app.extensions import db
import datetime


# class Rule(db.Model):
#     id = db.Column(db.Integer,primary_key=True)




# class Role(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     role = db.Column(db.String(30),nullable=False,unique=True)

#     def __repr__(self) -> str:
#         return f"{self.role}"
    


# # Define the UserRoles association table
# user_roles = db.Table(
#     "user_roles",
#     db.Column("user_id", db.ForeignKey('user.id', ondelete='CASCADE',primay=True)),
#     db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE',primary=True))
# )
    
    

class User(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(300))
    email = db.Column(db.String(300), unique=True,nullable=False)
    password = db.Column(db.String(300), nullable=False)
    is_admin = db.Column(db.Integer,default=0,nullable=True)


    # roles = db.relationship("Role",secondary="user_role",backref="users",lazy=True)
    # Define the relationship to Role via UserRoles
    # roles = db.relationship('Role', secondary='user_role')


    def __repr__(self) -> str:
        return f"<User: {self.email}>"
    

    @classmethod
    def get_all_users(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls,user_id):
        return cls.query.filter_by(id=user_id).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def get_user_for_auth(cls,email):
        user = cls.query.filter_by(email=email).first()
        return user



class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    category = db.Column(db.String(300),nullable=False,unique=True)

    quizes = db.relationship('Quiz', secondary='quiz_category')


    def __repr__(self) -> str:
        return f"<Category: {self.category}>"
    
    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls,category_id):
        return cls.query.get_or_404(category_id)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class QuizType(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    quiz_type = db.Column(db.String(300))



    def __repr__(self) -> str:
        return f"<QuizType: {self.quiz_type}>"
    

    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls,quiz_type_id):
        obj = cls.query.filter_by(id=quiz_type_id).first()
        return  obj
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()




class QuestionType(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    question_type = db.Column(db.String(300),nullable=False,unique=True)

    # quetions = db.relationship("QuizQuestion",backref='question_type',lazy=True)

    def __repr__(self) -> str:
        return f"<QuestionType: {self.question_type}>"


    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls,question_type_id):
        return cls.query.filter_by(id=question_type_id).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Quiz(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(300),unique=True)
    active = db.Column(db.String(),default=False)
    done = db.Column(db.String(),default=False)
    created_at = db.Column(db.String(100),default=datetime.datetime.now)

    categories = db.relationship('Category', secondary='quiz_category')
    
    user_id = db.Column(db.Integer,db.ForeignKey(User.id))
    user = db.relationship("User",backref=db.backref("quizes",lazy=True))

    quiz_type_id = db.Column(db.Integer,db.ForeignKey(QuizType.id))
    quiz_type = db.relationship("QuizType",backref=db.backref("quizes",lazy=True))

    # questions = db.relationship("QuizQuestion",backref="questions")

    def __repr__(self) -> str:
        return f"<Quiz: {self.title[:10]}>"
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls,quiz_id):
        return cls.query.filter_by(id=quiz_id).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

quiz_category = db.Table('quiz_category',
    db.Column('category_id', db.Integer, db.ForeignKey(Category.id), primary_key=True),
    db.Column('quiz_id', db.Integer, db.ForeignKey(Quiz.id), primary_key=True)
)




class QuizQuestion(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    question = db.Column(db.String(300),unique=True)
    choice1 = db.Column(db.String(500))
    choice2 = db.Column(db.String(500))
    choice3 = db.Column(db.String(500))
    choice4 = db.Column(db.String(500))
    correct_answer = db.Column(db.String(1))
    published = db.Column(db.String(),default=False)
    

    question_type_id = db.Column("question_type_id",db.ForeignKey(QuestionType.id))
    question_type = db.relationship('QuestionType',backref=db.backref("questions",lazy=True))

    quiz_id = db.Column("quiz_id",db.ForeignKey(Quiz.id))
    quiz = db.relationship("Quiz",backref=db.backref("questions",lazy=True))


    def __repr__(self) -> str:
        return f"<QuizQuestion: {self.question[:10]}>"
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls,question_id):
        return cls.query.get_or_404(question_id)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def get_question_by_quiz_id(cls,quiz_id):
        return cls.query.filter_by(quiz_id=quiz_id)



class QuizInstanceWithGrade(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column("user_id",db.ForeignKey(User.id))
    user = db.relationship(User,backref=db.backref("quizinstancegrades",lazy=True))

    quiz_id = db.Column("quiz_id",db.ForeignKey(Quiz.id))
    quiz = db.relationship(Quiz,backref=db.backref("quizinstancegrades",lazy=True))

    score_achived = db.Column(db.Integer)
    is_submitted = db.Column(db.Integer,default=0)
    is_active = db.Column(db.Integer,default = 0)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())


    def __repr__(self) -> str:
        return f"<QuizGrade {self.id}-{self.score_achived}"
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls,question_id):
        return cls.query.filter_by(question_id).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()



# class QuestionAnswer(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     user_id = db.Column("user_id",db.ForeignKey(User.id))
#     user = db.relationship(User,backref=db.backref("questionanswers",lazy=True))

#     quiz_id = db.Column("quiz_id",db.ForeignKey(Quiz.id))
#     quiz = db.relationship(Quiz,backref=db.backref("questionanswers",lazy=True))

#     question_id = db.Column(db.Integer,db.ForeignKey(QuizQuestion.id))
#     question = db.relationship(QuizQuestion,backref="questionanswers",lazy=True)
    
#     given_answer = db.Column(db.String())
#     created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())

#     def __repr__(self) -> str:
#         return f"<QuestionAnswer {self.question.question[:10]}-{self.given_answer}>"
    
#     @classmethod
#     def get_all(cls):
#         return cls.query.all()
    
#     @classmethod
#     def get_by_id(cls,question_answer_id):
#         return cls.query.filter_by(question_answer_id).first()
    
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
    
#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()




