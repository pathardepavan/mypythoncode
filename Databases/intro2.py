import psycopg2
class Student:
    def __init__(self):
        self.conn = psycopg2.connect(host='127.0.0.1',
                         user='devtools',
                         password='123',
                         database='tfa')
        self.cursor = self.conn.cursor()

    def read(self):
        self.cursor.execute("select * from students")
        for st in self.cursor.fetchall():
            print(st)

    def insert(self, name, email):
        query = "insert into students(name, email)" \
                "values('{}','{}')".format(name,email)
        self.cursor.execute(query)
        self.conn.commit()

    def update(self):
        pass

    def delete(self, email):
        query = "delete from students where email='{}'".format(email)
        self.cursor.execute(query)
        self.conn.commit()


if __name__=="__main__":
    x = Student()
    x.insert('test5','test5@gmail.com')
    x.delete('test5@gmail.com')