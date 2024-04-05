from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/test1')
def welcome_msg_1():
   return 'Welcome to the Sample Flask App'

#Without Decorator
def welcome_msg_2():
   return 'Welcome to the Sample Flask App - Without Decorator'

if __name__ == '__main__':
   
   app.add_url_rule(rule="/test2", view_func=welcome_msg_2)

   app.run(host='localhost', port=8100, debug=True)
   # debug=True will automatically reloads the application if any changes are made.
   
   