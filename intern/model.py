import sqlite3
import json
from datetime import datetime

def init_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM tabletodo")
    except:
        c.execute("CREATE TABLE tabletodo(id INTEGER PRIMARY KEY AUTOINCREMENT, itemName text, duedate real, status text);")
    conn.commit()
    conn.close()

def get_all_todos():
    conn=sqlite3.connect('todo.db')
    c=conn.cursor()
    results=c.execute("SELECT * FROM tabletodo;")
    todos=[]
    for item in results:
        todos.append([item[0],item[1],item[2],item[3]])
    return todos

def add_todo(todo):
    conn=sqlite3.connect('todo.db')
    c=conn.cursor()
    c.execute("INSERT INTO tabletodo(itemName,duedate,status) VALUES (?,?,?)",(todo[0],todo[1],todo[2],))
    conn.commit()
    conn.close()
    return

def update_status(status,id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("UPDATE tabletodo SET status = ? WHERE id = ?", (status,id))
    conn.commit()
    conn.close()
    return

def json_api():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    all_todos = c.execute("SELECT * FROM tabletodo;").fetchall()
    list_todos = []
    for todos in all_todos:
        dict_todo = {}
        dict_todo['id']=todos[0]
        dict_todo['name']=todos[1]
        dict_todo['duedate']=todos[2]
        dict_todo['status']=todos[3]
        list_todos.append(dict_todo)
    return json.dumps(list_todos)

def overdue():
    x = datetime.datetime.now().date()
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    duedate = c.execute("SELECT [id],[itemName],[duedate],[status] FROM tabletodo Where [duedate]<(:uname)",{'uname':x})
    list_date = []
    for todos in duedate:
        dict_todo = {}
        dict_todo['id']=todos[0]
        dict_todo['name']=todos[1]
        dict_todo['duedate']=todos[2]
        dict_todo['status']=todos[3]
        list_date.append(dict_todo)
    return json.dumps(list_date)

def finished():
    x = datetime.datetime.now().date()
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    duedate = c.execute("SELECT [id],[itemName],[duedate],[status] FROM tabletodo Where [status] ='finished'")
    list_date = []
    for todos in duedate:
        dict_todo = {}
        dict_todo['id']=todos[0]
        dict_todo['name']=todos[1]
        dict_todo['duedate']=todos[2]
        dict_todo['status']=todos[3]
        list_date.append(dict_todo)
    return json.dumps(list_date)
#
def task_list(date):
    # i = str(input())
    x =  datetime.strptime(date, '%Y-%m-%d').date()
    print(x)
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    task = c.execute("SELECT [id],[itemName],[duedate],[status] FROM tabletodo Where [duedate]=(:uname)",{'uname':x}).fetchall()
    list_date = []
    for todos in task:
        dict_todo = {}
        dict_todo['id']=todos[0]
        dict_todo['name']=todos[1]
        dict_todo['duedate']=todos[2]
        dict_todo['status']=todos[3]
        list_date.append(dict_todo)
    return json.dumps(list_date)


if __name__=='__main__':
    init_db()
    # print(get_all_todos())
