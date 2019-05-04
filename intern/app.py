from flask import Flask,request,render_template
# from flask_restplus import Api, Resource
import model

app = Flask(__name__)
# api = Api(app)
model.init_db()

@app.route("/api")
def api():
	return model.json_api()

@app.route("/api/overdue")
def api_overdue():
	return model.overdue()

@app.route("/api/finished")
def finished():
	return model.finished()

@app.route("/api/<date>")
def api_user(date):
	return model.task_list(date)

@app.route("/index")
def index():
	todos=model.get_all_todos()
	return render_template('index.html',todos=todos)


@app.route("/new")
def new():
	return render_template('form.html')

@app.route("/create", methods=["POST"])
def create():
	# todo = request.form.get("todo")
	todos = request.form['todo']
	todo_date = request.form['todo_date']
	status = request.form['status']
	todo = [todos,todo_date,status]
	model.add_todo(todo)
	return "database updated <a href='/index'> Return to Homepage</a>"


@app.route('/<int:id>', methods=["POST"])
def update(id):
	if request.method == 'POST':
		status = request.form['status']
		model.update_status(status,id)
		todos=model.get_all_todos()
		return render_template('index.html',todos=todos)


if __name__ == "__main__":
	app.run(debug=True)
