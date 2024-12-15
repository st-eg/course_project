from mysql.connector import connect, Error


class Con_base:
    def __init__(self):
        self.con = 0

    def con_base(self):
        try:
            self.con = connect(
                user='root',
                password='papa_dojo',
                host='localhost',
                db='cars'
            )
            print('Connection established *car*')
            return self.con
            self.cursor = self.con.cursor()
        except Error as e:
            print(e)

def base_demo():
            obj_bd = Con_base()
            obj = obj_bd.con_base()
            cur = obj.cursor()
            cur.execute('SELECT idCars, Make, Vehicle_Category from cars')
            list1 = cur.fetchall()
            print(list1)


db = Con_base()
db.con_base()
base_demo()
# db.base_demo()
# obj_bd = Con_base()


