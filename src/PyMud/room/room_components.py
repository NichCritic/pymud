'''
Created on 2013-11-15

@author: Nich
'''
from model.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

    
class Room(Base):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True)
    entity_id = Column(String, ForeignKey("entity.id"))


    def __init__(self, entity_id):
        self.entity_id = entity_id

   
    

components = {
}


db_components  = {
   "room":Room 
}


    
       
        