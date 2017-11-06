#!/usr/bin/python

from application import db



class Data(db.Model):
    ''' Model for one transaction - one entry in DB '''
    id = db.Column(db.Integer, primary_key=True)
    arabic = db.Column(db.Integer, index=True, unique=False)
    roman = db.Column(db.String(60))
    
    def __init__(self, roman, arabic):
        self.arabic = arabic
        self.roman = roman

    def __repr__(self):
        return '<Parsed: {} to {} >'.format(self.arabic, self.roman)


