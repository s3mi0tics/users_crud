from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("read_all.html", all_users = users)

# @app.route("/")
# def index():
#     # call the get all classmethod to get all friends
#     friends = Friend.get_all()
#     print(friends)
#     return render_template("index.html", friends = friends)

@app.route('/create')
def user_form():
    return render_template('/create.html')


@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

@app.route('/<int:id>/read_one')
def read_one(id):
    user = User.get_one({'id':id})
    return render_template('read_one.html', user = user)

@app.route('/<int:id>/update')
def update_form(id):
    data={
        "id":id
    }
    user = User.get_one(data)
    print("*****************")
    print(user.id)
    print(data["id"])
    return render_template('update.html', user = user)

    

@app.route('/user/update',methods=['POST'])
def update_one():
    print(request.form)
    User.update_one(request.form)
    return redirect('/')

@app.route('/<int:id>/delete')
def delete_one(id):
    data = {
        "id":id
    }
    User.delete_one(data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)