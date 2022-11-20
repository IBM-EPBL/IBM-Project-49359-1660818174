from flask import Flask,render_template,request,url_for,redirect
from flask_mail import *
from markupsafe import escape

import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30756;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=blk20068;PWD=LsEEBW71f9uXFNsf",'','')


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')      # index - home page

# admin credentials

@app.route('/adminlogin')

 def adminlogin():
  return render_template('adminlogin.html')   # admin log in page

@app.route('/adminreg')
def adminreg():
  return render_template('adminreg.html')  # admin sign up page


@app.route('/recipregistration')
def recipregistration():
  return render_template('recipregistration.html')   ## recipient signup page uh

@app.route('/recipientlogin')
def recipientlogin():
  return render_template('reclogin.html')      ## recipt login page


@app.route('/recipientrec',methods = ['POST', 'GET'])
def recipientrec():
  if request.method == 'POST':

    fname = request.form['fname']
    lname = request.form['lname']
    dob = request.form['dob']
    email = request.form['email']
    mnumb = request.form['mnumb']
    gender = request.form['gender']
    address = request.form['address']
    pin = request.form['pin']

    sql = "SELECT * FROM recipientrec WHERE fname =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,fname)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)


    if account:
       return render_template('reclogin.html', msg="Already your account exists, please try to log in")
    else:
     insert_sql = "INSERT INTO recipientrec VALUES (?,?,?,?,?,?,?,?)"
     prep_stmt = ibm_db.prepare(conn, insert_sql)
     ibm_db.bind_param(prep_stmt, 1, fname)
     ibm_db.bind_param(prep_stmt, 2, lname)
     ibm_db.bind_param(prep_stmt, 3, dob)
     ibm_db.bind_param(prep_stmt, 4, email)
     ibm_db.bind_param(prep_stmt, 5, mnumb)
     ibm_db.bind_param(prep_stmt, 6, gender)
     ibm_db.bind_param(prep_stmt, 7, address)
     ibm_db.bind_param(prep_stmt, 8, pin)
     ibm_db.execute(prep_stmt)
    
  return render_template('reclogin.html', msg="Account has been created successfully..")

  return "success..."


  ### donar crediential

@app.route('/donregistration')
def donregistration():
  return render_template('donregistration.html')   ## donar signup page uh


@app.route('/donarlogin')
def donarlogin():
  return render_template('donlogin.html')      ## donar login page


# @app.route('/donarrequest')
# def donarrequest():
#   return render_template('donar.html')  ## plasma requesting page


## donar details table

@app.route('/donrec',methods = ['POST', 'GET'])
def donrec():
  if request.method == 'POST':

    fname = request.form['fname']
    lname = request.form['lname']
    dob = request.form['dob']
    email = request.form['email']
    mnumb = request.form['mnumb']
    gender = request.form['gender']
    address = request.form['address']
    pin = request.form['pin']

    sql = "SELECT * FROM donarrec WHERE fname =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,fname)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)


    if account:
       return render_template('donlogin.html', msg="Already your account exists, please try to log in")
    else:
     insert_sql = "INSERT INTO donarrec VALUES (?,?,?,?,?,?,?,?)"
     prep_stmt = ibm_db.prepare(conn, insert_sql)
     ibm_db.bind_param(prep_stmt, 1, fname)
     ibm_db.bind_param(prep_stmt, 2, lname)
     ibm_db.bind_param(prep_stmt, 3, dob)
     ibm_db.bind_param(prep_stmt, 4, email)
     ibm_db.bind_param(prep_stmt, 5, mnumb)
     ibm_db.bind_param(prep_stmt, 6, gender)
     ibm_db.bind_param(prep_stmt, 7, address)
     ibm_db.bind_param(prep_stmt, 8, pin)
     ibm_db.execute(prep_stmt)
    
  return render_template('donlogin.html', msg="Account has been created successfully..")

  return "success..."


@app.route('/admin')
def admin():
  return render_template('admin.html')

@app.route('/donar')
def donar():
  return render_template('donar.html')


## donar registering for donation
@app.route('/giveplasma',methods = ['POST', 'GET'])
def giveplasma():
  if request.method == 'POST':

    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    mnumb = request.form['mnumb']
    email = request.form['email']
    city = request.form['city']
    address = request.form['address']
    bloodgroup = request.form['bloodgroup']
    issue = request.form['issue']
    lastbd = request.form['lastbd']
    slot = request.form['slot']

    sql = "SELECT * FROM donar WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,name)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('donlogin.html', msg="You are already a member, please login using your details")
    else:
      insert_sql = "INSERT INTO donar VALUES (?,?,?,?,?,?,?,?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, age)
      ibm_db.bind_param(prep_stmt, 3, gender)
      ibm_db.bind_param(prep_stmt, 4, mnumb)
      ibm_db.bind_param(prep_stmt, 5, email)
      ibm_db.bind_param(prep_stmt, 6, city)
      ibm_db.bind_param(prep_stmt, 7, address)
      ibm_db.bind_param(prep_stmt, 8, bloodgroup)
      ibm_db.bind_param(prep_stmt, 9, issue)
      ibm_db.bind_param(prep_stmt, 10, lastbd)
      ibm_db.bind_param(prep_stmt, 11, slot)
      ibm_db.execute(prep_stmt)
    
    return render_template('donar.html', msg="Your request for donation is successfully submitted..")

@app.route('/plasmadon')
def plasmadon():
  donar = []
  sql = "SELECT * FROM donar"
  stmt = ibm_db.exec_immediate(conn, sql)
  dictionary = ibm_db.fetch_both(stmt)
  while dictionary != False:
    # print ("The Name is : ",  dictionary)
    donar.append(dictionary)
    dictionary = ibm_db.fetch_both(stmt)

  if donar:
    return render_template("plasmadon.html", donar = donar)

@app.route('/delete/<name>')
def delete(name):
  sql = f"SELECT * FROM donar WHERE name='{escape(name)}'"
  print(sql)
  stmt = ibm_db.exec_immediate(conn, sql)
  donar = ibm_db.fetch_row(stmt)
  print ("The Name is : ",  donar)
  if donar:
    sql = f"DELETE FROM donar WHERE name='{escape(name)}'"
    print(sql)
    stmt = ibm_db.exec_immediate(conn, sql)

    donar = []
    sql = "SELECT * FROM donar"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
      donar.append(dictionary)
      dictionary = ibm_db.fetch_both(stmt)
    if donar:
      return render_template("plasmadon.html", donar = donar, msg="Delete successfully")


  
  # # while student != False:
  # #   print ("The Name is : ",  student)

  # print(student)
  return "success..."


@app.route('/mail')
def mail():
  return render_template('mail.html')

@app.route('/recipient')
def recipient():
  return render_template('recipient.html')


@app.route('/takeplasma',methods = ['POST', 'GET'])
def takeplasma():
  if request.method == 'POST':

    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    mnumb = request.form['mnumb']
    proof = request.form['proof']
    address = request.form['address']
    plasma = request.form['plasma']


    sql = "SELECT * FROM recipient WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,name)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('reclogin.html', msg="You are already a member, please login using your details")
    else:
      insert_sql = "INSERT INTO recipient VALUES (?,?,?,?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, age)
      ibm_db.bind_param(prep_stmt, 3, gender)
      ibm_db.bind_param(prep_stmt, 4, mnumb)
      ibm_db.bind_param(prep_stmt, 5, proof)
      ibm_db.bind_param(prep_stmt, 6, address)
      ibm_db.bind_param(prep_stmt, 7, plasma)
      ibm_db.execute(prep_stmt)
    
    return render_template('recipient.html', msg="Registration succesfull for Plasma request..")


@app.route('/plasmareq')
def plasmareq():
  recipient = []
  sql = "SELECT * FROM recipient"
  stmt = ibm_db.exec_immediate(conn, sql)
  dictionary = ibm_db.fetch_both(stmt)
  while dictionary != False:
    # print ("The Name is : ",  dictionary)
    recipient.append(dictionary)
    dictionary = ibm_db.fetch_both(stmt)

  if recipient:
    return render_template("plasmareq.html", recipient = recipient)


@app.route('/delete/<name>')
def deleted(name):
  sql = f"SELECT * FROM recipient WHERE name='{escape(name)}'"
  print(sql)
  stmt = ibm_db.exec_immediate(conn, sql)
  recipient = ibm_db.fetch_row(stmt)
  print ("The Name is : ",  recipient)
  if recipient:
    sql = f"DELETE FROM recipient WHERE name='{escape(name)}'"
    print(sql)
    stmt = ibm_db.exec_immediate(conn, sql)

    recipient = []
    sql = "SELECT * FROM recipient"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
      recipient.append(dictionary)
      dictionary = ibm_db.fetch_both(stmt)
    if recipient:
      return render_template("plasmareq.html", recipient = recipient, msg="Delete successfully")

    return "Deleted Successfully"


if __name__ == "__main__":
    app.run(debug=True)