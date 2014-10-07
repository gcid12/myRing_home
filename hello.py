from flask import Flask
from flask import render_template
from InsectData import InsectData

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def hello():
    title = 'MyRing'
    return render_template('home.html', title=title )

@app.route('/solutions')
def sol():
    insect = InsectData()
    il = {}

    il['spid'] = insect.spid()
    il['cica'] = insect.cica()

    dic = { 'r1': 'on', 
                'a1': il['spid']['title'],
                'a2': il['spid']['name'], 
                'a3': il['spid']['subtitle'],
                'a4': il['spid']['desc'], 
                'a5': il['spid']['label'], 
                'a6': il['spid']['icon'],
                'a7': il['spid']['preview'],
                'a8': il['spid']['slug'],
                # ---
                'b1': il['cica']['title'],
                'b2': il['cica']['name'], 
                'b3': il['cica']['subtitle'],
                'b4': il['cica']['desc'], 
                'b5': il['cica']['label'], 
                'b6': il['cica']['icon'],
                'b7': il['cica']['preview'],
                'b8': il['cica']['slug'],
                }

    return render_template('solutions.html', insects=il, dic=dic) 

@app.route('/solutions/model')
def solmod():

    insect = InsectData()
    il = {}

    il['spid'] = insect.spid()
    il['cica'] = insect.cica()

    dic = { 'r1': 'on', 
                'a1': il['spid']['title'],
                'a2': il['spid']['name'], 
                'a3': il['spid']['subtitle'],
                'a4': il['spid']['desc'], 
                'a5': il['spid']['label'], 
                'a6': il['spid']['icon'],
                'a7': il['spid']['preview'],
                'a8': il['spid']['slug'],
                # ---
                'b1': il['cica']['title'],
                'b2': il['cica']['name'], 
                'b3': il['cica']['subtitle'],
                'b4': il['cica']['desc'], 
                'b5': il['cica']['label'], 
                'b6': il['cica']['icon'],
                'b7': il['cica']['preview'],
                'b8': il['cica']['slug'],
                }

    return render_template('solutions.html', insects=il, dic=dic) 
    

@app.route('/solutions/capture')
def solcap():

    insect = InsectData()
    il = {}

    il['dfly'] = insect.dfly()
    il['mosq'] = insect.mosq()
    il['worm'] = insect.worm()

    dic = { 'r1': 'on', 
                'a1': il['dfly']['title'],
                'a2': il['dfly']['name'], 
                'a3': il['dfly']['subtitle'],
                'a4': il['dfly']['desc'], 
                'a5': il['dfly']['label'], 
                'a6': il['dfly']['icon'],
                'a7': il['dfly']['preview'],
                'a8': il['dfly']['slug'],
                # ---
                'b1': il['mosq']['title'],
                'b2': il['mosq']['name'], 
                'b3': il['mosq']['subtitle'],
                'b4': il['mosq']['desc'], 
                'b5': il['mosq']['label'], 
                'b6': il['mosq']['icon'],
                'b7': il['mosq']['preview'],
                'b8': il['mosq']['slug'],
                # ---
                'c1': il['worm']['title'],
                'c2': il['worm']['name'], 
                'c3': il['worm']['subtitle'],
                'c4': il['worm']['desc'], 
                'c5': il['worm']['label'], 
                'c6': il['worm']['icon'],
                'c7': il['worm']['preview'],
                'c8': il['worm']['slug'],
                }

    return render_template('solutions.html', insects=il, dic=dic) 


@app.route('/solutions/expose')
def solexp():
    insect = InsectData()
    il = {}

    il['bees'] = insect.bees()
    il['lbug'] = insect.lbug()
    il['bfly'] = insect.bfly()

    dic = { 'r1': 'on', 
                'a1': il['bees']['title'],
                'a2': il['bees']['name'], 
                'a3': il['bees']['subtitle'],
                'a4': il['bees']['desc'], 
                'a5': il['bees']['label'], 
                'a6': il['bees']['icon'],
                'a7': il['bees']['preview'],
                'a8': il['bees']['slug'],
                # ---
                'b1': il['lbug']['title'],
                'b2': il['lbug']['name'], 
                'b3': il['lbug']['subtitle'],
                'b4': il['lbug']['desc'], 
                'b5': il['lbug']['label'], 
                'b6': il['lbug']['icon'],
                'b7': il['lbug']['preview'],
                'b8': il['lbug']['slug'],
                # ---
                'c1': il['bfly']['title'],
                'c2': il['bfly']['name'], 
                'c3': il['bfly']['subtitle'],
                'c4': il['bfly']['desc'], 
                'c5': il['bfly']['label'], 
                'c6': il['bfly']['icon'],
                'c7': il['bfly']['preview'],
                'c8': il['bfly']['slug'],
                }

    return render_template('solutions.html', insects=il, dic=dic)        

# TOOOOOOLLLLLLSSSSSSSSTOOOOOOLLLLLLSSSSSSSS 

#m-arana / TOCA
@app.route('/tools/schema_modeler') 
def spid():
    dic = { 'r1': 'on',
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
    dic = { 'r1': 'on', 
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
    dic = { 'r1': 'on', 
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
    dic = { 'r1': 'on', 
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
    dic = { 'r1': 'on', 
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
    dic = { 'r1': 'on', 
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
    dic = { 'r1': 'on', 
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
    dic = { 'r1': 'on', 
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
