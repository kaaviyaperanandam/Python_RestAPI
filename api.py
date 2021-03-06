from flask import Flask,jsonify,request           #importing Flask ,jsonify and request Classes
app=Flask(__name__)                               # creating instance of flask class
serials=[{'hero':'Green Arrow'},{'hero':'Flash'},{'hero':'Batman'}]     #such as a json format

#Get method i.e. Select operation

@app.route('/',methods=['GET'])      # defining route
def test():                         # method to link with route
    return jsonify({'message':'It works'})

@app.route('/test',methods=['GET'])
def getAll():
    return jsonify({'Series':serials})

@app.route('/test/<string:hero>',methods=['GET'])   #route defined with some id
def getById(hero):
    series=[episode for episode in serials if episode['hero']==hero]      #searching with some id
    return jsonify({'Series':series[0]})                                  #returning available searched dictionary based on  id
########################################################################################################################

# Post method  i.e. insert operation

@app.route('/test',methods=['POST'])
def addOne():
    series={'hero':request.json['hero']}   #here key will be hero and value will be fetched from json data based on its key
    serials.append(series)                 #appending specified data to existing one
    return jsonify(serials)

# Put method i.e. Update operation

@app.route('/test/<string:hero>',methods=['PUT'])
def updateOne(hero):
    series=[episode for episode in serials if episode['hero']==hero]
    series[0]['hero']=request.json['hero']
    return jsonify({'hero':'series[0]'})

# Delete method i.e. Delete operation

@app.route('/test/<string:hero>',methods=['DELETE'])
def deleteOne(hero):
    series = [episode for episode in serials if episode['hero'] == hero]
    serials.remove(series[0])
    return jsonify({'Serials':serials})


#the below line says that our python program can act as standalone or reusable program
# visit for more help ---- http://effbot.org/pyfaq/tutor-what-is-if-name-main-for.htm
if __name__=='__main__':
    app.run(debug=True)  #running app in debugging mode

