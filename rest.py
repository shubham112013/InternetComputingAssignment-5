from flask import Flask, request,Response
from Agent import Service
import json
app=Flask(__name__)
service = Service()

@app.route('/agent/<string:agentid>',methods=['GET','DELETE','PUT'])
def get_agent(agentid):
    if request.method=='GET':
        return Response(json.dumps(service.get_agent(agentid)),mimetype='application/json')
    elif request.method=='DELETE':
        service.remove_agent(agentid)
    elif request.method=='PUT':
        service.update_agent(agentid,request.get_json())
    return 'updated'

@app.route('/agent',methods=['GET','POST'])
def get_agents():
    if request.method=='POST':
        service.add_agent(request.get_json())
    return Response(json.dumps(service.get_agents()),mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
