import mysql.connector 
# pip install mysql-connector 


try:
    db= mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    db='project'
    )
    print("Connected Successfully")
except Exception as e:
    print("Database Not connected: ",e)

cursor= db.cursor()

def loginAdmin(data):
    print(data)
    try:
        cursor.execute('select * from admin where name= %s and password= %s',data)
        return cursor.fetchone()
    except Exception as e:
        print("Error is ",e)
        return False
def registerUser(data):
    try:
        cursor.execute("INSERT into user(name,age,email,password,gender,dob,weight,height,phonenumber,photo) Values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",data)
        db.commit()
        return True
    except Exception as e:
        print("Error is-",e)
        return False
    
def getallusers(data):
    print(data)
    try:
        cursor.execute('select * from trainer where email= %s and password= %s',data)
        return cursor.fetchone()
    except Exception as e:
        print("Error is ",e)
        return False
    
# to get tariner 
def getallpeople(data):
    print(data)
    try:
        cursor.execute('Select * from user where email=%s and password=%s',data)
        return cursor.fetchone()
    except Exception as e:
        print("Error is ",e)
        return False


    
def updateuser(data):
    try:
        print(data)
        cursor.execute('update user set name=%s,age=%s,email=%s,password=%s,gender=%s,dob=%s,weight=%s,height=%s,phonenumber=%s,photo=%s where id=%s',data)
        db.commit()
        return True
    except Exception as e:
        print("Error is",e)
        return False
def updatetrainer(data):
    try:
        print(data)
        cursor.execute('update trainer set name=%s,email=%s,password=%s,age=%s,gender=%s,dob=%s,address=%s,mobile_number=%s,years_of_experience=%s,preferred_communication_language=%s,photo=%s where id=%s',data)
        db.commit()
        return True
    except Exception as e:
        print("Error is",e)
        return False

    
def registertrainer(data):
    try:
        cursor.execute('INSERT into trainer(name,email,password,age,gender,dob,address,mobile_number,years_of_experience,preferred_communication_language,photo) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',data)
        db.commit()
        return True
    except Exception as e:
        print("Error is-",e)
        return False
        
def savebmi(id,data):
    try:
        cursor.execute('INSERT into diet(id, bmi) Values(%s,%s)',(id,data))
        db.commit()
        return True
    except Exception as e:
        print("Error is",e)
        return False

def bmi(data,id):
    try:
        cursor.execute("UPDATE  diet SET bmi=%s WHERE id=%s", (data[2], id))
        db.commit()
        return True
    except Exception as e:
        print("Error is",e)
        return False
    
    # def diet(data):
    # try:
    #     cursor.execute('INSERT into diet(client_id,diet,photo) Values(%s, %s,%s)',data)
    #     db.commit()
    #     return True
    # except Exception as e:
    #     print("Error is",e)
    #     return False
def diet(data,id):
    try:
        cursor.execute("UPDATE diet SET diet=%s WHERE id=%s", (data[1], id))
        db.commit()
        return True
    except Exception as e:
        print("Error is",e)
        return False
def getdiet(id):
    try:
        cursor.execute('Select * from diet where id=%s',(id,))
        result= cursor.fetchone()
        if result:
            return result[2]
        else:
            return None
        
    except Exception as e:
        print("Error is",e)
        return None
def getbmi(id):
    try:
        cursor.execute('Select * from diet where id=%s',(id,))
        result= cursor.fetchone()
        if result:
            return result[1]
        else:
            return None
        
    except Exception as e:
        print("Error is",e)
        return None

def getAllTrainers():
    try:
        cursor.execute('Select * from trainer')
        return cursor.fetchall()
    except Exception as e:
        print("Error is",e)
        return False
def getAllUser():
    try:
        cursor.execute('Select * from user')
        return cursor.fetchall()
    except Exception as e:
        print("Error is",e)
        return False
    
def nameTask():
    try:
        cursor.execute('SELECT id,name from trainer')
        return cursor.fetchall()
    except:
        return False
    
def nameEmp():
    try:
        cursor.execute('SELECT id,Name from user')
        return cursor.fetchall()
    except:
        return False
    
def deleteTrainer(data):
    try:
        cursor.execute('delete from trainer where id=%s',data)
        db.commit()
        return True
    except Exception as e:
        print("Error is",e)
        return False
        
def deleteUser(data):
    try:
        cursor.execute('delete from user where id=%s',data)
        db.commit()
        return True
    except Exception as e:
        print("Error is",e)
        return False
        
        
def assignTrainer(arg):
    try:
        # print(arg)
        cursor.execute("INSERT INTO assign (custid,trainerid) VALUES (%s,%s)", arg)
        db.commit()
        return True
    except:
        print("Error is",e)
        return False


def deleteAssign(data):
    try:
        cursor.execute('delete from assign where id=%s',data)
        db.commit()
        return True
    except Exception as e:
        print("Error is",e)
        return False
    
def allassignTrainer():
    try:
        cursor.execute('Select * from assign')
        return cursor.fetchall()
    except Exception as e:
        print("Error is",e)
        return False


def query_clients_for_trainer(trainer_id):
    print("Id is -----",trainer_id)
    
    query = """
        SELECT user.id, user.name, user.email, user.phonenumber, user.weight, user.height, user.photo
        FROM assign
        INNER JOIN user ON assign.custid = user.id
        WHERE assign.trainerid = %s
    """
    cursor.execute(query, (trainer_id,))
    clients = cursor.fetchall()
    return clients
        
