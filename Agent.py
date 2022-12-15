from tinydb import TinyDB, Query,where

db = TinyDB('db.json')
agent = Query()

class Service:

    def get_agent(self,agentid):
        return db.search(agent.id==agentid)

    def get_agents(self):
        return db.all()

    def add_agent(self,data):
        db.insert(data)

    def remove_agent(self,agentid):
        db.remove(agent.id==agentid)

    def update_agent(self,agentid,data):
        db.update(data,where('id')==agentid)
