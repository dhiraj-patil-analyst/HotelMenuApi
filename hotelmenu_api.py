from flask import Flask,request
app=Flask(__name__)
items=[{
       "Name":"Misalpav",
        "Price":20
       },
       {"Name":"Samosa",
       "Price":20},
       {"Name":"Biryani","Price":140}
]


@app.get('/get-items')
def get_all_items():
  return {"Items":items}

# for dynamic url

''' @app.get('/get-item/<string:name>')
def get_item (name):
    for item in items:
         if name == item['Name']:
             return item
    return {'message':"Record doesn't exist"}    '''

# For key value addition method

          
@app.get('/get-item')
def get_item ():
    Name=request.args.get('Name')
    for item in items:
         if Name == item['Name']:
             return item
    return {'message':"Record doesn't exist"} ,404

@app.post('/add-items')
def add_item():
    request_data=request.get_json()
    items.append(request_data)
    return {"message":"Item added successfully!"},201

@app.put('/update-item')
def update_item():
    request_data=request.get_json()
    for item in items:
        if item['name']==request_data['name']:
            item['price']=request_data['price']
            return {"message":"Item updated successfully!"}
    return {'Message':"Record doesn't exist"},404



if __name__=="__main__":
  app.run(debug=True)
  
  
  
  
  
  
  
  
  