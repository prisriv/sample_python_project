from DBHelper import DBHelper

def main():
    db=DBHelper() 
    while True:
        print("Enter your choice")
        print("1. Insert product")
        print("2. Display products")
        print("3. Delete product")
        print("4. Update product")
        print("5. Exit")
    try:
        choice=int(input())
        if (choice==1):
            pid=int(input("Enter product id"))
            pname=input("Enter product name")
            pprice=int(input("Enter product price"))
            db.insert_product(pid,pname,pprice)
        elif choice==2:
            db.fetch_all()
        elif choice==3:
            pid=int(input("Enter user id which you want to delete"))
            db.delete_product(pid)
        elif choice==4:
            pid=int(input("Enter product id"))
            pname=input("Enter product name to update")
            pprice=int(input("Enter product price to update"))
                db.update_product(pid,pname,pprice)
        elif choice==5:
            break
        else:
            print("Invalid input")
    except Exception as e:
        print(e)
        print("Invalid details, try again")


       
#helper.insert_product(123,"mobile phone",10000)
#helper.delete_product(123)
#helper.fetch_all()
#helper.update_product(123,"laptop",20000)
#helper.fetch_all()

if __name__=="__main__":
    main()