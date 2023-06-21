#Membership
from datetime import date

def add():
    code_m=input("code_meli:")
    if code_m not in list_c:
        list_c.append(code_m)
        f_name=input("f_name:")
        l_name=input("l_name:")
        address=input("address:")
        new = date.today()
        
        list_f.append(f_name)
        list_L.append(l_name)
        list_a.append(address)
        list_t.append(new)
        list_code.append("c"+code_m)
        
def display(list_c):
    for i in range(len(list_c)):
        print(f"name{i+1}:{list_f[i]}, {list_L[i]},{list_code[i]},{list_t[i]}")

def edit(list1):
    for i in list1:
        c=input("cod_melii:")
        if c not in list_c:
            list_c[i]=c
            f=input("f_name:")
            l=input("l_name:")
            a=input("address:")
            list_L[i]=l or list_L[i]
            list_f[i]=f or list_f[i]
            list_a[i]=a or list_a[i]
            print("edited")
        else:
            print(f"{c}:mojod ast")
        
    
def remove(list2):
    for i in list2:
        g = list_c.index(i)
        list_c.remove(i)
        list_t.pop(g)
        
        list_a.pop(g)
        list_f.pop(g)
        list_code.pop(g)
        print("done")

#books
def add_book():
    p_id=input("id_book:")
    if p_id not in books.keys():
        name = input("book name: ")
        name_writer =(input("name_writer: "))
        year=(input("sall entshsar: "))
        fild= input("book fild: ")
        book = {
			"name" : name,
			"name_writer" : name_writer,
			"year" : year,
			"fild" : fild
		}
        books[p_id] = book
    else:
        print(f"{p_id}:exist!")
    
def display_book():
	for key, value in books.items():
		print(key)
		for x, y in value.items():
			print(f"{x} ---> {y}")
		print(20 * "-")

def remove_book(list1):
    for i in list1:
        if i in books.keys():
            books.pop(i)
        else:
            print("not found!")
            
def edit_book(list1):
    for i in list1:
        if i in books.keys():
            info=input("information for edit[name,name_writer,year,fild]")
            info=info.split()
            books["name"]=info[0] or books["name"]
            books["name_writer"]=info[1] or books["name_writer"]
            books["year"]=info[2] or books["year"]
            books["fild"]=info[3] or books["fild"]
            print("edited")
        else:
           print("not found!")


def find_book(cood):
   
    list_amanat.append(cood)
    
    for book in books.values():
        for code in book.values():
            if cood == code:
                return 1
            else:
                return -1


def amanat():
    if find_book==1:
       cood_user=input("cood_user:")             
       if cood_user in list_code:
           cood_book=input("cood_book")
           tarikh_t=input("tarikh_t[//]")
           tarikh_b=input("tarikh_b[//]")
    else:
        print("not found!")

def serch_book():
    if find_book==1:
        for book in books.values():
            for code in book.values():
                if cood == code:
                    print(book)
    else:
        print("not found!")
        

list_c=[]
list_a=[]
list_L=[]
list_f=[]
list_code=[]
list_t=[]
list_amanat=[]
books={}
while True:
    user=input("add,remove,edit,display,exit remove_book,add_book,edit_book,display_book,serch_book,amanat,display_amanat,help:")
    if user=="add":
        add()
    elif user=="remove":
        display(list_c)
        num=input("number:")
        list2=[list_c[int(i)-1] for i in num.split()] 
        remove(list2)
    elif user=="edit":
        display(list_c)
        x=input("number:")
        list1=[int(i)-1 for i in x.split()]
        edit(list1)   
    elif user=="exit":
        break
    elif user=="":
        pass
    elif user=="display":
        display(list_c)
    elif user=="add_book":
        add_book()
    elif user=="remove_book":
        display_book()
        p_ids=input("p_ids to remove_book:")
        p_ids=p_ids.split()
        remove_book(p_ids)
    elif user=="edit_book":
        display_book()
        p_ids=input("p_ids to edit_book:")
        p_ids=p_ids.split()
        edit_book(p_ids)
    elif user=="display_book":
        display_book()
    elif user=="serch_book":
        cood=input("name_book or fild_book:") 
        find_book(cood) 
        serch_book()
    elif user=="amanat":
        cood=input("name_book or fild_book:") 
        find_book(cood) 
        amanat()
    elif user=="display_amanat":
        print(list_amanat)  
    elif user=="help":
        print("add:add user; /n remove:Delet user; /n edit:edit user information; /n add_book:add book; /n remove_book:Delet book; /n edit_book:edit book information; /n display_book:show the list of book; /n display:show member list; /n amanat:brrowing books; /n serch_book:Book search based on name and field; /n display_amanat: display of loaned books; /n exit: exit the program")  
    else:
        print("comand not found")