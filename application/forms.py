#!/usr/bin/python

from flask.ext.wtf import Form
from wtforms import TextField, validators

''' Input forms on the UI '''

class EnterDBInfo(Form):
    dbNotes = TextField(label='Enter the integer', description="db_enter", validators=[validators.required(), validators.Regexp('^\d{1,4}$',message=u'Enter a number between 1 and 10000')])


class RetrieveDBInfo(Form):
   numRetrieve = TextField(label='Number of DB Items to Get', description="db_get", validators=[validators.required(), validators.Regexp('^\d{1}$',message=u'Enter a number between 1 and 10')])
