from flask import Flask, render_template, request
from application import db
from application.models import Data
from application.forms import EnterDBInfo, RetrieveDBInfo
from application.worker import roman_parse

'''
Flask application micro app boilerplate for Roman Numerals Coding Challenge 

Boilerplate enables it to be easily be deployed on Amazon Elastic Beanstalk

This module exposes an API endpoint with GET and POST methods.

The flow is open to public, no registration.

User lands on a page where there is a field for the arabic number to be parsed to roman repr.

User submits the number , gets redirected to thanks.html with last result.

It's a simplistic API, you can do one parsing at a time, and retrieve a list with 9 last entries. 

Author: Ismar Sehic - i.sheeha@gmail.com

More Info in README.md
'''

# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug = True

application.secret_key = 'cC2YCIWOj9GgWspgNEo2'


@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    form1 = EnterDBInfo(request.form)
    form2 = RetrieveDBInfo(request.form)

    if request.method == 'POST' and form1.validate():
        number = int(form1.dbNotes.data)
        parsed = roman_parse(number)
        data_entered = Data(arabic=number, roman= parsed)
        try:
            db.session.add(data_entered)
            db.session.commit()
            db.session.close()
        except:
            db.session.rollback()

        data = 'Parsed: {} to {} '.format(number, parsed)
        return render_template('thanks.html', data=data)

    if request.method == 'POST' and form2.validate():

        num_return = int(form2.numRetrieve.data)
        query_db = Data.query.order_by(Data.id.desc()).limit(num_return)

        results = [q for q in query_db] or []

        import ipdb; ipdb.set_trace()
        if results is not []:
            db.session.close()

        else:
            db.session.rollback()

        return render_template('results.html', results=results, num_return=num_return)

    return render_template('index.html', form1=form1, form2=form2)


if __name__ == '__main__':
    application.run(host='0.0.0.0')
