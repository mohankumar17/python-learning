from flask import Flask, request

app = Flask(__name__)

@app.route('/api/calculate/<operation>', methods = ['POST'])
def calculate(operation='add'):
   try:
      res = 0
      response_body_json = {}
      error_response = {}
      
      if request.is_json:
         request_body_json = request.json # Data in JSON format
         num1 = request_body_json["num1"]
         num2 = request_body_json["num2"]
      else:
         error_response = {
            "success": "false",
            "message": "Input must of type application/json"
         }
         return error_response, 415

      if operation == "add":
         res = num1 + num2
      elif operation == "subtract":
         res = num1 - num2
      elif operation == "multiply":
         res = num1 * num2
      elif operation == "divide":
         res = num1 / num2
      else:
         #raise ValueError("Invalid Operator")
         res = None

      if res is None:
         error_response = {
            "success": "false",
            "message": "Wrong operation. API supports only add, subtract, multiply and divide."
         }
         return error_response
         
      response_body_json = {
         "success": "true",
         "num1": num1,
         "num2": num2,
         "operation": operation,
         "result": res
      }
      return response_body_json
   
   except Exception as ex:
      error_response = {
         "success": "false",
         "message": "Other error",
         "exception": ex.args
      }
      return error_response, 500

if __name__ == '__main__':
   app.run(host='localhost', port=8100, debug=True)