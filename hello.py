from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def hello():
    title = 'MyRing'
    return render_template('home.html', title=title )

@app.route('/solutions')
def sol():
    dic = {	'r1': 'on', 
    			'a1': 'Schema Modeler',
    			'a2': 'TOCATL v.0.2.3', 
    			'a3': 'Model and edit your schemas .',
    			'a4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
    			'a5': 'Modeling Solution', 
    			'a6': 'r-spider.png', 
    			'a7': 'phiw/ph01.png', 
    			'b1': 'Semantic labeler',
    			'b2': 'CHIQUILICHTLI v.0.1.1', 
    			'b3': 'Create rich semantic Data',
    			'b4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
    			'b5': 'Modeling Solution', 
    			'b6': 'r-cicada.png', 
    			'b7': 'phiw/ph02.png',
    			}
    return render_template('solutions.html', dic=dic) 

@app.route('/solutions/model')
def solmod():
    dic = {	'r1': 'on', 
    			'a1': 'Schema Modeler',
    			'a2': 'TOCATL v.0.2.3', 
    			'a3': 'Model and edit your schemas .',
    			'a4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
    			'a5': 'Modeling Solution', 
    			'a6': 'r-spider.png', 
    			'a7': 'phiw/ph01.png', 
    			'b1': 'Semantic labeler',
    			'b2': 'CHIQUILICHTLI v.0.1.1', 
    			'b3': 'Create rich semantic Data',
    			'b4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
    			'b5': 'Modeling Solution', 
    			'b6': 'r-cicada.png', 
    			'b7': 'phiw/ph02.png', 
    			}
    return render_template('solutions.html', dic=dic) 

@app.route('/solutions/capture')
def solcap():
    dic = {	'r2': 'on', 
    			'a1': 'Manual Capture',
    			'a2': 'ETZATL v.0.1.2', 
    			'a3': 'Capture all kind of Data manually',
    			'a4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
    			'a5': 'Modeling Solution', 
    			'a6': 'r-vespa.png', 
    			'a7': 'phiw/ph05.png', 
    			'b1': 'Automatic Capture',
    			'b2': 'APIPILO v.0.1.2', 
    			'b3': 'Capture your Data via sensors and devices.',
    			'b4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
    			'b5': 'Modeling Solution', 
    			'b6': 'r-mosco.png', 
    			'b7': 'phiw/ph11.png', 
    			'c1': 'Legacy Data',
    			'c2': 'TEMOLIN 0.1.2', 
    			'c3': "Bring your legacy Data back to life",
    			'c4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
    			'c5': 'Modeling Solution', 
    			'c6': 'r-worm.png', 
    			'c7': 'phiw/ph03.png',  
    			}
    return render_template('solutions.html', dic=dic) 

@app.route('/solutions/expose')
def solexp():
    dic = {	'r3': 'on', 
    			'a1': 'Data Expose',
    			'a2': 'TLALPIPIOLLI v.1.2.0', 
    			'a3': 'Serve your Data in REST and multiple formats',
    			'a4': 'Design a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
    			'a5': 'Modeling Solution', 
    			'a6': 'r-bee.png', 
    			'a7': 'diagram.png', 
    			'b1': 'Data combinator',
    			'b2': 'MICAZOYOLIN 0.1.2', 
    			'b3': 'Modeling schemas have never been easier, modelo its about being happy.',
    			'b4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
    			'b5': 'Modeling Solution', 
    			'b6': 'r-ladybug.png', 
    			'b7': 'diagram.png', 
    			'c1': 'Data Merger',
    			'c2': 'PAPALOTL v.0.1.2', 
    			'c3': 'Modeling schemas have never been easier, modelo its about being happy.',
    			'c4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
    			'c5': 'Modeling Solution', 
    			'c6': 'r-bfly.png', 
    			'c7': 'diagram.png',  
    			}
    return render_template('solutions.html', dic=dic)         

@app.route('/details')
def detai():
    dic = {	'r1': 'on', 
    			'a1': 'Legacy Data',
    			'a2': 'TEMOLIN 0.1.2', 
    			'a3': 'Bring your legacy Data back to life.',
    			'a4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
    			'a5': 'Capture Solution', 
    			'a6': 'r-worm.png', 
    			'a7': 'Ipsum Lorem',
    			'a8': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a9': 'phiw/ph03.png',
    			'a10': 'Ipsum Lorem',
    			'a11': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a12': 'phiw/ph06.png', 
    			'a13': 'Ipsum Lorem ',
    			'a14': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a15': 'phiw/ph07.png',
    			
    			}
    return render_template('details.html', dic=dic)  

@app.route('/pricing')
def prici():
    title = 'My Ring Pricing'
    return render_template('pricing.html', title=title) 

@app.route('/combos')
def combo():
    title = 'My Combos'
    return render_template('combos.html', title=title)                

@app.route('/docs')
def docs():
    title = 'Documentation'
    return render_template('docs.html', title=title) 

@app.route('/images')
def hello_images():
    title = 'My Ring Solutions'
    return 'Showing Images!'

@app.route('/vespa/<id>')
def hello_image_id(id):
    name = 'Ricardo'
    apellido = 'Cid'
    print('huevos')
    #return 'hola2'+id
    return render_template('avispa.html', name=name)

if __name__ == '__main__':
    app.run()
