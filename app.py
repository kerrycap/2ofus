from flask import Flask, render_template, url_for, request, redirect
"""from flask_sqlalchemy import SQLAlchemy"""
from datetime import datetime
import pandas as pd

app = Flask(__name__)


"""app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)"""

import datetime
today = datetime.date.today()
thisyear = today.year
timeleft = int

"""
class userdata():
    aname = (db.String)
    asex = (db.String)
    abirth = (db.Integer)
    bname = (db.String)
    bsex = (db.String)
    bbirth = (db.Integer)
    abyear = (db.Integer)
    thisyear=today.year
"""

"""
def __repr__(self):
    return '<task %r>' % self.id
"""
@app.route('/learnmore')
def learnmore():
    return render_template('learnmore.html')


@app.route('/',methods=['GET','POST'])
def index():
    try:
        SSA_Table = pd.read_excel ('lifeexpectancy.xlsx')
        if request.method=='POST':
            bbirth=int(request.form['bbirth'])
            abirth=int(request.form['abirth'])
            aname=(request.form['aname'])
            bname=(request.form['bname'])
            abyear=int(request.form['abyear'])
            bsex=(request.form['bsex'])
            asex=(request.form['asex'])
            aage = thisyear-abirth
            bage = thisyear-bbirth
            yearstogether = thisyear-abyear

            if abirth>abyear or bbirth>abyear:
                return render_template('error.html')

            if asex in ['male']:
                alife=int(SSA_Table.iloc[aage, 1])
            else:
                alife=int(SSA_Table.iloc[aage,3])


            if bsex in ['male']:
                blife=int(SSA_Table.iloc[bage, 1])
            else:
                blife=int(SSA_Table.iloc[bage,3])

            timeleft=min(alife,blife)

            if timeleft<yearstogether:
                return render_template('results.html', aname=aname, bname=bname, aage=aage, bage=bage, alife=alife, blife=blife, yearstogether=yearstogether, timeleft=timeleft)
            else:
                return render_template('results2.html', aname=aname, bname=bname, aage=aage, bage=bage, alife=alife, blife=blife, yearstogether=yearstogether, timeleft=timeleft)
    except:
        return render_template('error.html')


    else:
            return render_template('index.html')







"""
return f'{bname} has a life expectancy of another {blife} years.'
        return f'{aname} is about {aage} years old and {bname} is about {bage} years old. You have already known each other for {yearstogether} years.'
        return f'{aname} has a life expectancy of another {alife} years.'
def yearsleft(abirth, bbirth):
    bbirth=int(request.form['bbirth'])
    abirth=int(request.form['abirth'])
    aage = thisyear-abirth
    bage = thisyear-bbirth

    return(aage,bage)
"""
"""
        aname=request.form['aname']
        bname=request.form['bname']
        asex=request.form['asex']
        bsex=request.form['bsex']
        abirth=request.form['abirth']
        bbirth=request.form['bbirth']
        abyear=request.form['abyear']
        thisyear=thisyear
"""


"""
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem'

@app.route('/update/<int:id>', methods =['GET', 'POST'])
def update(id):
     task = Todo.query.get_or_404(id)
     if request.method == 'POST':
         task.content = request.form['content']

         try:
             db.session.commit()
             return redirect('/')
         except:
             return 'There was an issue with updating'
     else:
         return render_template('update.html', task=task)
"""
"""
if __name__ == "__main__":
    app.run(debug=True)
"""
