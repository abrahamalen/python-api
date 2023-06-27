from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-user/<user_id>')
def get_user(user_id):
    user_data = {
        'user_id': user_id,
        'name': 'John Doe',
        'age': 30,
        'city': 'New York',
        'email': 'johndoe@unknown.com' 
    }

    extra = request.args.get('extra')
    if extra:
        user_data['extra'] = extra

    return jsonify(user_data), 200
 
@app.route('/create-user', methods=['POST'])
def create_user():
    data = request.get_json()

    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)




# HTTP Methods
# GET -> Request a data from a specifed resource
# POST -> Submit data to be processed to a specified resource
# PUT -> Update a specified resource
# DELETE -> Delete a specified resource
# PATCH -> Update a specified resource
# OPTIONS -> Retrive the supported HTTP methods
# HEAD -> Retrive the headers for a specified resource
# CONNECT -> Establish a tunnel to the server identified by the target resource
# TRACE -> Perform a message loop-back test along the path to the target resource

# Status Codes
# 1xx -> Informational
# 2xx -> Success
# 3xx -> Redirection
# 4xx -> Client Error
# 5xx -> Server Error

# 200 -> OK
# 201 -> Created
# 202 -> Accepted
# 204 -> No Content
# 301 -> Moved Permanently
# 302 -> Found
# 304 -> Not Modified
# 400 -> Bad Request
# 401 -> Unauthorized
# 403 -> Forbidden
# 404 -> Not Found
# 405 -> Method Not Allowed
# 500 -> Internal Server Error
# 501 -> Not Implemented
# 503 -> Service Unavailable