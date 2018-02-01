from flask import Flask, render_template, request 
from sqlalchemy import create_engine 
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///./test.db'  



db = SQLAlchemy(app)
# concerns=[]1
# class Users(db.Model):.
# 	 __tablename__ = "Users_data"
# 	 id= db.Column('id', db.Integer, primary_key=True)


class Concern(db.Model):
    __tablename__ = "Concernss"
    id = db.Column('id', db.Integer, primary_key=True)
    # username = db.Column(db.String(15))
    concern = db.Column(db.String(100))
    answer= db.Column(db.String(100))
    # password= db.Column(db.String(100)).

    def __init__(self,concern):
    	self.concern= concern
    	# self.password=password

# class Answers(db.Model):
# 	__tablename__="answers"
# 	answer=db.Answers(db.String(100))
# 	id= db.Column('id', db.Integer, primary_key=True)
# 	answer_id = db.Column(db.Integer, ForeignKey('Concernss.id'), nullable=False)
# 	userR = relationship('answers', foreign_keys='Concernss.user_id')



db.create_all()


@app.route('/')
def index():
	return render_template('SignUp.html')

@app.route('/InWhy')
def InWhy():
	return render_template('contact_us.html')

@app.route('/WelcomeToHomePage', methods=['post'])
def WelcomeToHomePage():
	# Login=request.form['login']
	# Password=request.form['password']
	# reg= Login(login)
	# reg= Password(password)
	# db.session.add(reg)
	# db.session.commit()
	return render_template('HOMEPAGE.html')



@app.route('/add_post' , methods=['POST'])
def add_post():
	concern= request.form['concern']
	# concerns.append({'concern': concern})
	reg= Concern(concern)
	db.session.add(reg)
	db.session.commit()
	concerns=Concern.query.all()
	return render_template('Homefeed.html', concerns=concerns)

@app.route('/answer_concern', methods=['POST'])
def answer_concern():
	answers= request.form['answer']
	id_concern=request.form['id']
	single_concern=Concern.query.filter_by(id=id_concern).first()
	single_concern.answer = answers
	print(single_concern.answer)
	db.session.commit()
	concerns = Concern.query.all()
	return render_template('Homefeed.html', concerns=concerns)


	
db.create_all()
