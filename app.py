from flask import Flask,render_template,request,session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user
from random import *  
import smtplib
import random

local_server= True
app = Flask(__name__)
app.secret_key='fingerprintatm'

# this is for getting unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/fatm'
db = SQLAlchemy(app)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)
    eimg= db.Column(db.String(100), unique=True, nullable=False)
class Admin(db.Model):
    
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False,primary_key=True)

class Acct(db.Model):
    aid = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(100), unique=True, nullable=False)
    cno = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    ccvv = db.Column(db.String(100), unique=True, nullable=False)
    ced = db.Column(db.String(100), unique=True, nullable=False)
    camt = db.Column(db.String(100), unique=True, nullable=False)

class Trans(db.Model):
    tid = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    ctype = db.Column(db.String(100), unique=True, nullable=False)
    camt = db.Column(db.String(100), unique=True, nullable=False)




@app.route("/")
def home():
    return render_template("home.html")

@app.route("/vtrans")
def vtrans():
    data=db.engine.execute(f"select * from `acct`")
    return render_template("/vtrans.html",data1=data)
    

@app.route("/acctdetails",methods=['POST','GET'])
def acctdetails():
    if request.method=='POST':
        
        cname=request.form.get("cname")
        cno=request.form.get("cno")
        email=request.form.get("email")
        ccvv=request.form.get("ccvv")
        ced=request.form.get("ced")
        camt=float(request.form.get("camt"))
        acct=Acct.query.filter_by(email=email).first()
        new_acct=db.engine.execute(f"INSERT INTO `acct`(`cname`,`cno`,`email`,`ccvv`,`ced`,`camt`)VALUES('{cname}','{cno}','{email}','{ccvv}','{ced}','{camt}')")
        
        return render_template("/acctdetails.html",a="money added successfully")   
    return render_template("acctdetails.html")

@app.route("/update",methods=['POST','GET'])
def update():
    print("hiiiiiiiiiiiii")
    em=current_user.email
    data=db.engine.execute(f"select * from `acct` where email='{em}' ")
    print(data)
    return render_template("update2.html",data=data)

@app.route("/update2",methods=['POST','GET'])
def update2():
    
    if request.method=='POST':
        em=current_user.email 
        camt=float(request.form.get("camt"))
        
        pamt=db.engine.execute(f"select camt from acct where email='{em}'")
        ppamt=pamt.fetchall()
        db.engine.execute(f"update acct set camt={camt}+{ppamt[0][0]} where email='{em}'")
        data=db.engine.execute(f"select * from acct")
        print(data)

        return render_template("acctdetails.html",a="Money updated successfully")
        
  
    return render_template("update2.html")

@app.route("/menu2")
def menu2():
    return render_template("menu2.html")

@app.route("/admin",methods=['POST','GET'])
def admin():
    if request.method=='POST':
        username=request.form.get("username")
        password=request.form.get("password")
        aadmin=Admin.query.filter_by(username=username,password=password).first()
        if aadmin:
            return render_template("/menu2.html")
        else:
            return render_template("/admin.html",a="Invalid username & password")
    
    return render_template("admin.html")

@app.route("/signup",methods=['POST','GET'])
def signup():
    if request.method=='POST':
        username=request.form.get("username")
        email=request.form.get("email")
        password=request.form.get("password")
        eimg=request.form.get("eimg")
        user=User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first() or User.query.filter_by(password=password).first() or User.query.filter_by(eimg=eimg).first()
        if user:
            
            print("user already Exist")
            return render_template("/signup.html",a="User Already Exist")

        new_user=db.engine.execute(f"INSERT INTO `user`(`username`,`email`,`password`,`eimg`)VALUES('{username}','{email}','{password}','{eimg}')")
        return render_template("/login.html")   
    return render_template("signup.html")

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method=='POST':
        email=request.form.get("email")
        password=request.form.get("password")
        eimg=request.form.get("eimg")
        user=User.query.filter_by(email=email,password=password,eimg=eimg).first()
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('sirchandana0987654321@gmail.com','iqpalrygmrnosvov')
        msg='Hello your otp is '+str(otp)
        server.sendmail(email,email,msg)
        server.quit()
        print(msg)
        if user and password:
            login_user(user)           
            return render_template("/uverify.html")
        else:
            return render_template("/login.html",a="Invalid User")
    return render_template("login.html")

@app.route("/uverify",methods=['POST','GET'])
def uverify():
        
    uotp=request.form.get("otp")
    if otp==uotp:
        return render_template("menu.html",a="Transaction Success")
        
    else:
        return render_template("uverify.html",a="Invalid OTP") 

@app.route("/vusers")
def vusers():
    data=db.engine.execute(f"select * from `user`")
    return render_template("/vusers.html",data1=data)

@app.route("/vmoney")
def vmoney():
    em=current_user.email
  
  
    data=db.engine.execute(f"select * from `acct` where email='{em}'")
   

    return render_template("/vmoney.html",data1=data)
 

otp=''.join([str(random.randint(0,9)) for i in range(4)])

@app.route("/transfer",methods=['POST','GET'])
def transfer():
    
    
    if request.method=='POST':
        
        em=current_user.email
        an = request.form['anum'];
        wamt=int(request.form.get("wamt"))
  
  
        ct=db.engine.execute(f"select camt from `acct` where `email`='{em}'")
        camt=ct.fetchall()
        
        ##target user
        try:
            tu = db.engine.execute(f"select camt from acct where cno = {an}")
            tamt = tu.fetchall()
            val = tamt[0][0]
            val = int(val)+wamt
            db.engine.execute(f"update acct set camt={val} where cno={an}")
        except Exception as e:
            return render_template("/transfer.html",a="Please enter the correct details")
        ##changes end
        
        cname=request.form.get("cname")
        email=request.form.get("email")
        
        
        if wamt>int(camt[0][0]):
            db.engine.execute(f"select * from `acct`")
            return render_template("/transfer.html",a="Insufficient fund")
        ndata=db.engine.execute(f"select {int(camt[0][0])}-{wamt} from `acct` where email='{em}' ")
        nwd=ndata.fetchall()

        data=db.engine.execute(f"update `acct` SET camt='{nwd[0][0]}'  where email='{em}' ")

        
        return render_template("/transfer.html",a="Transfer success")   
        

    return render_template("/transfer.html")


if __name__ == "__main__":
    app.run(debug=True)




