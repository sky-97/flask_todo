# Flask Todo application

Flask ToDo  is application, built with help of flask, Where user can add there Task and status to help them keep track of daily obligations.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

What things you need to install the software and how to install them

``` pip3 install flask ```
##### You just need to install flask library and for database i am gonna  use ``` sqlite3 ``` no need to install sqlite module It is included in the standard library (since Python 2.5)

### File Structure

 ``` /foldername ```
         ``` -app.py ```
        ```  -model.py ```
         ``` /templates ```
             ``` -base.html ```
             ``` -form.html ```
             ``` -index.html ```
             
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
