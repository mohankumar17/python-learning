import requests
url = "https://jsonplaceholder.typicode.com/posts"

#title = input("Enter title of the post: ")
#attributes = {"title": title}
id = input("Enter ID of the post: ")

try:
    #resp = requests.get(url, attributes)
    resp = requests.get(url+"/"+id)
    if resp.status_code == 200:
        #print("Response in raw format:", resp.text)
        print("Response in JSON format:", resp.json())
        print("Headers: ",resp.headers)
        print("Media Type:", resp.headers['Content-Type'])
except Exception as e:
    print(e)