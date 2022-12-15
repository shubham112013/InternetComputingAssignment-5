from flask import redirect,Flask, render_template, request
import requests

app = Flask(__name__)
url='http://172.17.0.1:4000'
@app.route('/')
def get_agent_list():
    data = requests.get(url=url+'/agent').json()
    return render_template('/agent.html',result=data)

@app.route('/add',methods = ['POST', 'GET'])
def result():
   if request.method == 'GET':
      return render_template("add.html")
   else:
       data = request.form
       requests.post(url=url+'/agent',json={"id":data['id'],"agentname":data['agentname'] ,"ontrip":data['ontrip'],"order-id":data['order-id'],"pick":data['pick'],"drop":data['drop']})
       return redirect('/')

@app.route('/delete/<string:agentid>')
def remove(agentid):
    requests.delete(url=url+'/agent/'+agentid)
    return redirect('/')

@app.route('/update',methods=['POST'])
def update():
    data=request.form
    requests.put(url=url+'/agent/'+data['id'],json={"id":data['id'],"agentname":data['agentname'] ,"ontrip":data['ontrip'],"order-id":data['order-id'],"pick":data['pick'],"drop":data['drop']})
    return redirect('/')

@app.route('/agent/<string:agentid>')
def get_employee(agentid):
    data = requests.get(url=url + '/agent/'+agentid).json()
    return render_template('/update.html',result=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
