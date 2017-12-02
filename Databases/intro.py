#Database
#You willl have package psycopg2 <pip install psycopg2>
#Python APplication
import psycopg2
option = int(input("1.Read\n2.Insert\n3.Update\n4.Delete\nEnter Option:"))
#Connect
conn = psycopg2.connect(host='127.0.0.1',
                         user='devtools',
                         password='123',
                         database='tfa')
try:

    if option == 1:
        #Read Code
        cursor = conn.cursor()
        query = "select * from students"
        cursor.execute(query)
        # fetchall, fetchone, fetchmany
        result = cursor.fetchall()
        for st in result:
            print(st)
    elif option==2:
        #Insert Code
        #First get the name and email from end user
        #prepare the query
        #execute the query
        name = input("Enter name:")
        email = input("Enter email:")
        query = "insert into students(name, email)values('{}','{}')".format(name,
                                                                            email)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("inserted")
    elif option==3:
        #Update Code
        #get the email to update
        #Search the students for email, if not found give message
        #if found ask new name to udpate
        #prepare the query, run the query and provide message
        #commit
        pass
    elif option==4:
        #Delete Code
        #get the email to delete
        #check in database, if not found give info
        #delete, commit and provide message
        pass
    else:
        print("Wrong option.Try again")

except Exception as e:
    print(e)
finally:
    conn.close()

