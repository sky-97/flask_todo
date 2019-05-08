# Flask Todo application

Flask ToDo  is application, built with help of flask, Where user can add there Task and status to help them keep track of daily obligations.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine .

## Prerequisites

What things you need to install the software and how to install them

``` pip3 install flask ```
##### You just need to install flask library and for database i am gonna  use ``` sqlite3 ``` no need to install sqlite module It is included in the standard library (since Python 2.5)

### File Structure

``` ├── app.py
 
    ├── model.py
    
    │
    
    ├── templates
    
    │   ├── base.html
    
    │   ├── form.html
    
    │   └── index.html
    
    └── todo.db

app.py is a ```controller``` in which all logics are there, model.py is a ```model``` file in which all database insert create and querry codes  are there, temaplates is a folder inside which there is ```view``` files.
      
### Running the tests

```python app.py ```

##### As i am following ``` MVC ```  Model-View-Controller framework MVC Controllers are responsible for controlling the flow of the application execution. When you make a request (means request a page) to MVC application, a controller is responsible for returning the response to that request, Here app.py is my controller thats why i am runing app.py file

## Running the tests

#### A link will appear in your terminal, copy the link and paste it in web browser

http://127.0.0.1:5000/index

``` /index  ```
#### ```/index``` is a page, in this page all your ToDo List in form of tables will appear when you add a new ToDo Task

#### If you need to make a new todo task, click on ``` create new todo ``` when you click on the link you will be redirect to new page ``` /new ```, where you need to add todo task, name, date and status, then click on button ``` create todo ``` 
#### Then you will redirect to ``` /create ``` page where will get the message database updated,when you click on return to homepage then you can see the todo list which made eariler , In index page we also have authorization to edit status of the task.

### How to use API?

##### Basically, an API specifies how software components should interact. Additionally, APIs are used when programming graphical user interface (GUI) components. A good API makes it easier to develop a program by providing all the building blocks. A programmer then puts the blocks together.Here we getting it in form of [JSON](https://jsonapi.org/)

``` /api ```
##### In this page will get all the task inserted in database in form of key and value(JSON)

``` /api/overdue ```

##### In this page all the ```overdue``` status will be displyed

```/api/finished ```

##### In this page all the  ```finished``` status will be displayed

``` /api/<date> ```

##### If need to findout the status and task of the any dates then you need to add example -```/api/2019-01-01 ``` it will display that date status and task, if not avilable then it will show empty.(date year and month should be in form of ```yyyy-mm-dd```)

## Built With
 
 [FLask](http://flask.pocoo.org/)
 
 [SQLite](https://www.sqlite.org/index.html)
 
 [MVC](https://flask-diamond.readthedocs.io/en/latest/model-view-controller/)
 
 [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 
 [Bootstrap](https://getbootstrap.com/)
