from flask import Flask, request

app = Flask(__name__)

# Set WSGI_HEADERS_PREFIX to empty string to forward all headers
app.config['WSGI_HEADERS_PREFIX'] = ''

# URI Parameters
@app.route('/api/<id>')
def fun_uri_param(id):
   return 'ID: ' + id

@app.route('/api/<id>/<name>')
def fun_uri_params_2(id, name):
   return id + " " + name

# Query Parameters
@app.route('/api')
def fun_query_params():
   activeStatus = request.args.get("isActive") 
   date = request.args["dateAfter"]
   
   return activeStatus + " " + date

# Headers
@app.route('/api/v2')
def fun_headers():
   
   request_headers = dict(request.headers)
   print(request_headers)

   #accept_encodings = request.accept_encodings
   #print(accept_encodings)

   #client_id = request.headers.get('client_id')
   #print(client_id)
   #client_secret = request.headers.get("client_secret")
   return "Success"

# HTTP Methods
@app.route('/api/users', methods = ['GET', 'POST'])
def get_users():
    if request.method == "GET":
       return 'Fetched all users', 200
    else:
       return 'Added user details', 201

# Request Body
@app.route('/api/add', methods = ['POST'])
def add_nums():
   res = 0
   
   print(request.data) # Data in raw format
   print(request.is_json)
   print(request.mimetype)
   
   request_body_json = request.json # Data in JSON format
   print(request_body_json)

   res = request_body_json["num1"] + request_body_json["num2"]
   return "Sum: " + str(res)

if __name__ == '__main__':
   app.run(host='localhost', port=8100, debug=True)
   
   