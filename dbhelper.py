import mysql.connector as connector
class DBHelper:
    #initialize connection string
    def __init__(self):
        self.con=connector.connect
        (host='localhost',port='3306',user='root',database='sampleproductdb')
        query='create table if not exists product(productid int primary_key,productname varchar(200),price int)'
        self.con.cursor()
        cur.execute(query)
        print("Created")
    
    #insert operation
    def insert_product(self,productid,productname,price)
        query="insert into product(productid,productname,price)
        values({},'{}',{})".format(productid,productname,price)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        cur.commit()
        print("product added to db")
    
    #select
    def fetch_all(self):
        query="select * from product"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)
    
    #delete
    def delete_product(self,productid):
        query="delete from product where productid={}".format(productid)
        print(query)
        self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("product deleted")

    #update
    def update_product(self,productid,newname,newprice):
        query="update user set productname={},price={} where productid={}".format(newname,newprice)
        print(query)
        cur=self.con.cursor
        cur.execute(query)
        self.con.commit()
        print("product updated")