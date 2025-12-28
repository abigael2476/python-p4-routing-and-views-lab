from flask import Flask

app = Flask(__name__)

# 1. Index route
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


# 2. Print string route
@app.route("/print/<string:param>")
def print_string(param):
    print(param)
    return param


# 3. Count route (with trailing newline)
@app.route("/count/<int:param>")
def count(param):
    result = ""
    for i in range(param):
        result += f"{i}\n"
    return result


# 4. Math route
@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        return str(num1 / num2)
    elif operation == "%":
        return str(num1 % num2)
    else:
        return "Invalid operation"


if __name__ == "__main__":
    app.run(debug=True)
