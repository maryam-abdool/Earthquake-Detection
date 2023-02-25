from app import app 
from flask import render_template
from flask import request 

extra_users = []

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    user = {
        "nickname": "Users"
    }
    title = "DevFest 2023"
    posts = [
        {
            "author": {
                "nickname": "User1"
            }, 
            "body": {
                "I'm User1."
            }
        },
        {
            "author": {
                "nickname": "User2"
            }, 
            "body": {
                "I'm User2."
            }
        },
    ]
    if (request.method == "POST"):
        user = request.form.get("user number")
        extra_users.append(user)
        for user in extra_users:
            posts.append(
                {
                    "author": {
                    "nickname": "User{}".format(user)
                    }, 
                    "body": {
                        "I'm User{}.".format(user)
                    }
                }
            )
    return render_template("index.html", title=title, user=user, posts=posts)