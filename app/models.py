import datetime

from flask_appbuilder import Model
from sqlalchemy import Column, Date, Integer, Float

class Cislo(Model):
    id = Column(Integer, primary_key=True)
    cislo = Column(Float)

    def __repr__(self):
        return self.cislo