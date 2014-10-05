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
    			'a6': 'r-spid.png', 
    			'a7': 'phiw/ph01.png',
    			'a8': 'schema_modeler',
    			# ---
    			'b1': 'Semantic labeler',
    			'b2': 'CHIQUILICHTLI v.0.1.1', 
    			'b3': 'Create rich semantic Data',
    			'b4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
    			'b5': 'Modeling Solution', 
    			'b6': 'r-cica.png', 
    			'b7': 'phiw/ph02.png',
    			'b8': 'semantic_labeler', 
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
    			'a6': 'r-spid.png', 
    			'a7': 'phiw/ph01.png', 
    			'a8': 'schema_modeler',
    			# --- 
    			'b1': 'Semantic labeler',
    			'b2': 'CHIQUILICHTLI v.0.1.1', 
    			'b3': 'Create rich semantic Data',
    			'b4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
    			'b5': 'Modeling Solution', 
    			'b6': 'r-cica.png', 
    			'b7': 'phiw/ph02.png',
    			'b8': 'semantic_labeler', 
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
    			'a6': 'r-wasp.png', 
    			'a7': 'phiw/ph05.png',
    			'a8': 'manual_capture', 
    			# ---
    			'b1': 'Automatic Capture',
    			'b2': 'APIPILO v.0.1.2', 
    			'b3': 'Capture your Data via sensors and devices.',
    			'b4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
    			'b5': 'Modeling Solution', 
    			'b6': 'r-mosq.png', 
    			'b7': 'phiw/ph11.png',
    			'b8': 'automatic_capture',  
    			# ---
    			'c1': 'Legacy Data',
    			'c2': 'TEMOLIN 0.1.2', 
    			'c3': "Bring your legacy Data back to life",
    			'c4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
    			'c5': 'Modeling Solution', 
    			'c6': 'r-worm.png', 
    			'c7': 'phiw/ph03.png', 
    			'c8': 'legacy_data', 
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
    			'a6': 'r-bees.png', 
    			'a7': 'diagram.png',
    			'a8': 'data_expose', 
    			# ---
    			'b1': 'Data combinator',
    			'b2': 'MICAZOYOLIN 0.1.2', 
    			'b3': 'Modeling schemas have never been easier, modelo its about being happy.',
    			'b4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
    			'b5': 'Modeling Solution', 
    			'b6': 'r-lbug.png', 
    			'b7': 'diagram.png',
    			'b8': 'data_combinator', 
    			# ---
    			'c1': 'Data Merger',
    			'c2': 'PAPALOTL v.0.1.2', 
    			'c3': 'Modeling schemas have never been easier, modelo its about being happy.',
    			'c4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
    			'c5': 'Modeling Solution', 
    			'c6': 'r-bfly.png', 
    			'c7': 'diagram.png', 
    			'c8': 'data_merger',  
    			}
    return render_template('solutions.html', dic=dic)         

# TOOOOOOLLLLLLSSSSSSSSTOOOOOOLLLLLLSSSSSSSS 

#m-arana / TOCA
@app.route('/tools/schema_modeler') 
def spid():
    dic = {	'r1': 'on',
    			'a1': 'Schema Modeler',
                'a2': 'TOCATL v.0.2.3', 
                'a3': 'Model and edit your schemas .',
                'a4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
                'a5': 'Modeling Solution', 
                'a6': 'r-spid.png',
    			'a7': '1Ipsum Lorem',
    			'a8': '1Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a9': 'phiw/ph03.png',
    			'a10': '2Ipsum Lorem',
    			'a11': '2Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a12': 'phiw/ph06.png', 
    			'a13': '3Ipsum Lorem ',
    			'a14': '3Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a15': 'phiw/ph07.png',
    			}
    return render_template('details.html', dic=dic)  

#m-cicada  /  CHIQ
@app.route('/tools/semantic_labeler')
def cica():
    dic = {	'r1': 'on', 
    			'a1': 'Semantic labeler',
                'a2': 'CHIQUILICHTLI v.0.1.1', 
                'a3': 'Create rich semantic Data',
                'a4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
                'a5': 'Modeling Solution', 
                'a6': 'r-cica.png',  
    			'a7': '1Ipsum Lorem',
    			'a8': '1Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a9': 'phiw/ph03.png',
    			'a10': '2Ipsum Lorem',
    			'a11': '2Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a12': 'phiw/ph06.png', 
    			'a13': '3Ipsum Lorem ',
    			'a14': '3Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a15': 'phiw/ph07.png',
    			}
    return render_template('details.html', dic=dic) 

#c-avispa  /  ETZA
@app.route('/tools/manual_capture')
def wasp():
    dic = {	'r1': 'on', 
    			'a1': 'Manual Capture',
                'a2': 'ETZATL v.0.1.2', 
                'a3': 'Capture all kind of Data manually',
                'a4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
                'a5': 'Modeling Solution', 
                'a6': 'r-wasp.png', 
    			'a7': '1Ipsum Lorem',
    			'a8': '1Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a9': 'phiw/ph03.png',
    			'a10': '2Ipsum Lorem',
    			'a11': '2Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a12': 'phiw/ph06.png', 
    			'a13': '3Ipsum Lorem ',
    			'a14': '3Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a15': 'phiw/ph07.png',
    			}
    return render_template('details.html', dic=dic) 

#c-mosquitoe   /  APIP
@app.route('/tools/automatic_capture')
def mosq():
    dic = {	'r1': 'on', 
    			'a1': 'Automatic Capture',
                'a2': 'APIPILO v.0.1.2', 
                'a3': 'Capture your Data via sensors and devices.',
                'a4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
                'a5': 'Modeling Solution', 
                'a6': 'r-mosq.png',  
    			'a7': '1Ipsum Lorem',
    			'a8': '1Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a9': 'phiw/ph03.png',
    			'a10': '2Ipsum Lorem',
    			'a11': '2Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a12': 'phiw/ph06.png', 
    			'a13': '3Ipsum Lorem ',
    			'a14': '3Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a15': 'phiw/ph07.png',
    			}
    return render_template('details.html', dic=dic)  


#c-worm   /  TEMO
@app.route('/tools/legacy_data')
def worm():
    dic = {	'r1': 'on', 
    			'a1': 'Legacy Data',
                'a2': 'TEMOLIN 0.1.2', 
                'a3': "Bring your legacy Data back to life",
                'a4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
                'a5': 'Modeling Solution', 
                'a6': 'r-worm.png', 
    			'a7': '1Ipsum Lorem',
    			'a8': '1Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a9': 'phiw/ph03.png',
    			'a10': '2Ipsum Lorem',
    			'a11': '2Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a12': 'phiw/ph06.png', 
    			'a13': '3Ipsum Lorem ',
    			'a14': '3Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a15': 'phiw/ph07.png',
    			}
    return render_template('details.html', dic=dic)   

#e-bee  /  TLAL
@app.route('/tools/data_expose')
def bees():
    dic = {	'r1': 'on', 
    			'a1': 'Data Expose',
                'a2': 'TLALPIPIOLLI v.1.2.0', 
                'a3': 'Serve your Data in REST and multiple formats',
                'a4': 'Design a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
                'a5': 'Modeling Solution', 
                'a6': 'r-bee.png', 
    			'a7': '1Ipsum Lorem',
    			'a8': '1Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a9': 'phiw/ph03.png',
    			'a10': '2Ipsum Lorem',
    			'a11': '2Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a12': 'phiw/ph06.png', 
    			'a13': '3Ipsum Lorem ',
    			'a14': '3Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a15': 'phiw/ph07.png',
    			}
    return render_template('details.html', dic=dic)  

#e-ladybug  /  MICA
@app.route('/tools/data_combinator')
def lbug():
    dic = {	'r1': 'on', 
    			'a1': 'Data combinator',
                'a2': 'MICAZOYOLIN 0.1.2', 
                'a3': 'Modeling schemas have never been easier, modelo its about being happy.',
                'a4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
                'a5': 'Modeling Solution', 
                'a6': 'r-lbug.png', 
    			'a7': '1Ipsum Lorem',
    			'a8': '1Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a9': 'phiw/ph03.png',
    			'a10': '2Ipsum Lorem',
    			'a11': '2Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a12': 'phiw/ph06.png', 
    			'a13': '3Ipsum Lorem ',
    			'a14': '3Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a15': 'phiw/ph07.png',
    			}
    return render_template('details.html', dic=dic)  

#e-Butterfly   /   PAPA
@app.route('/tools/data_merger')
def bfly():
    dic = {	'r1': 'on', 
    			'a1': 'Data Merger',
                'a2': 'PAPALOTL v.0.1.2', 
                'a3': 'Modeling schemas have never been easier, modelo its about being happy.',
                'a4': 'Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ', 
                'a5': 'Modeling Solution', 
                'a6': 'r-bfly.png', 
    			'a7': '1Ipsum Lorem',
    			'a8': '1Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a9': 'phiw/ph03.png',
    			'a10': '2Ipsum Lorem',
    			'a11': '2Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
    			'a12': 'phiw/ph06.png', 
    			'a13': '3Ipsum Lorem ',
    			'a14': '3Designing a system that deal with data is not an easy task, it involves putting up with different data formats, modeling flexible schemas, data versioning, analisys. ',
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
