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

    dic = { 'a1': il['spid']['title'],
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

    dic = { 'a1': il['spid']['title'],
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
    il['ants'] = insect.ants()

    dic = { 'a1': il['dfly']['title'],
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
            'c1': il['ants']['title'],
            'c2': il['ants']['name'], 
            'c3': il['ants']['subtitle'],
            'c4': il['ants']['desc'], 
            'c5': il['ants']['label'], 
            'c6': il['ants']['icon'],
            'c7': il['ants']['preview'],
            'c8': il['ants']['slug'],
            # ---
            'd1': il['worm']['title'],
            'd2': il['worm']['name'], 
            'd3': il['worm']['subtitle'],
            'd4': il['worm']['desc'], 
            'd5': il['worm']['label'], 
            'd6': il['worm']['icon'],
            'd7': il['worm']['preview'],
            'd8': il['worm']['slug'],
                }

    return render_template('solutions.html', insects=il, dic=dic) 


@app.route('/solutions/share')
def solsha():
    insect = InsectData()
    il = {}

    il['bees'] = insect.bees()
    il['lbug'] = insect.lbug()
    il['bfly'] = insect.bfly()

    dic = { 'a1': il['bees']['title'],
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
    insect = InsectData()
    il = {}

    il['spid'] = insect.spid()
    il['cica'] = insect.cica()


    dic = { 'a1': il['spid']['title'],
            'a2': il['spid']['name'], 
            'a3': il['spid']['subtitle'],
            'a4': il['spid']['desc'], 
            'a5': il['spid']['label'], 
            'a6': il['spid']['icon'],
            'a7': il['spid']['preview'],
            'a8': il['spid']['slug'],
            'a9': il['spid']['step1'],
            'a10': il['spid']['diag1'], 
            'a11': il['spid']['step2'],
            'a12': il['spid']['diag2'], 
            'a13': il['spid']['step3'], 
            'a14': il['spid']['diag3'],
            #
            'b1': il['cica']['title'], 
            'b2': il['cica']['icon'],
            'b3': il['cica']['slug'],
                }

    return render_template('details.html', insects=il, dic=dic)  

#m-cicada  /  CHIQ
@app.route('/tools/semantic_labeler')
def cica():
    insect = InsectData()
    il = {}

    il['spid'] = insect.spid()
    il['cica'] = insect.cica()

    dic = { 'a1': il['cica']['title'],
            'a2': il['cica']['name'], 
            'a3': il['cica']['subtitle'],
            'a4': il['cica']['desc'], 
            'a5': il['cica']['label'], 
            'a6': il['cica']['icon'],
            'a7': il['cica']['preview'],
            'a8': il['cica']['slug'],
            'a9': il['cica']['step1'],
            'a10': il['spid']['diag1'], 
            'a11': il['spid']['step2'],
            'a12': il['spid']['diag2'], 
            'a13': il['spid']['step3'], 
            'a14': il['spid']['diag3'],
            #
            'b1': il['spid']['title'], 
            'b2': il['spid']['icon'],
            'b3': il['spid']['slug'],
                }

    return render_template('details.html', insects=il, dic=dic) 

#c-avispa  /  ETZA
@app.route('/tools/manual_capture')
def dfly():
    insect = InsectData()
    il = {}

    il['dfly'] = insect.dfly()
    il['mosq'] = insect.mosq()
    il['worm'] = insect.worm()
    il['ants'] = insect.ants()

    dic = { 'a1': il['dfly']['title'],
            'a2': il['dfly']['name'], 
            'a3': il['dfly']['subtitle'],
            'a4': il['dfly']['desc'], 
            'a5': il['dfly']['label'], 
            'a6': il['dfly']['icon'],
            'a7': il['dfly']['preview'],
            'a8': il['dfly']['slug'],
            'a9': il['dfly']['step1'],
            'a10': il['dfly']['diag1'], 
            'a11': il['dfly']['step2'],
            'a12': il['dfly']['diag2'], 
            'a13': il['dfly']['step3'], 
            'a14': il['dfly']['diag3'],
            #
            'b1': il['mosq']['title'], 
            'b2': il['mosq']['icon'],
            'b3': il['mosq']['slug'],
            'b1': il['mosq']['title'],
            # 
            'c1': il['worm']['title'], 
            'c2': il['worm']['icon'],
            'c3': il['worm']['slug'],
            'c1': il['worm']['title'],
            #
            'd1': il['ants']['title'], 
            'd2': il['ants']['icon'],
            'd3': il['ants']['slug'],
            'd1': il['ants']['title'],

                }

    return render_template('details.html', insects=il, dic=dic)  

#c-mosquitoe   /  APIP
@app.route('/tools/automatic_capture')
def mosq():
    insect = InsectData()
    il = {}

    il['dfly'] = insect.dfly()
    il['mosq'] = insect.mosq()
    il['worm'] = insect.worm()
    il['ants'] = insect.ants()

    dic = { 'a1': il['mosq']['title'],
            'a2': il['mosq']['name'], 
            'a3': il['mosq']['subtitle'],
            'a4': il['mosq']['desc'], 
            'a5': il['mosq']['label'], 
            'a6': il['mosq']['icon'],
            'a7': il['mosq']['preview'],
            'a8': il['mosq']['slug'],
            'a9': il['mosq']['step1'],
            'a10': il['mosq']['diag1'], 
            'a11': il['mosq']['step2'],
            'a12': il['mosq']['diag2'], 
            'a13': il['mosq']['step3'], 
            'a14': il['mosq']['diag3'],
            #
            'b1': il['dfly']['title'], 
            'b2': il['dfly']['icon'],
            'b3': il['dfly']['slug'],
            'b1': il['dfly']['title'],
            # 
            'c1': il['worm']['title'], 
            'c2': il['worm']['icon'],
            'c3': il['worm']['slug'],
            'c1': il['worm']['title'],
            #
            'd1': il['ants']['title'], 
            'd2': il['ants']['icon'],
            'd3': il['ants']['slug'],
            'd1': il['ants']['title'],
                }

    return render_template('details.html', insects=il, dic=dic)  


#c-worm   /  TEMO
@app.route('/tools/legacy_data')
def worm():
    insect = InsectData()
    il = {}

    il['dfly'] = insect.dfly()
    il['mosq'] = insect.mosq()
    il['worm'] = insect.worm()
    il['ants'] = insect.ants()

    dic = { 'a1': il['worm']['title'],
            'a2': il['worm']['name'], 
            'a3': il['worm']['subtitle'],
            'a4': il['worm']['desc'], 
            'a5': il['worm']['label'], 
            'a6': il['worm']['icon'],
            'a7': il['worm']['preview'],
            'a8': il['worm']['slug'],
            'a9': il['worm']['step1'],
            'a10': il['worm']['diag1'], 
            'a11': il['worm']['step2'],
            'a12': il['worm']['diag2'], 
            'a13': il['worm']['step3'], 
            'a14': il['worm']['diag3'],
            #
            'b1': il['mosq']['title'], 
            'b2': il['mosq']['icon'],
            'b3': il['mosq']['slug'],
            'b1': il['mosq']['title'],
            # 
            'c1': il['dfly']['title'], 
            'c2': il['dfly']['icon'],
            'c3': il['dfly']['slug'],
            'c1': il['dfly']['title'],
            #
            'd1': il['ants']['title'], 
            'd2': il['ants']['icon'],
            'd3': il['ants']['slug'],
            'd1': il['ants']['title'],
                }

    return render_template('details.html', insects=il, dic=dic) 

#c-ant   /  TEMO
@app.route('/tools/data_scrapper')
def ants():
    insect = InsectData()
    il = {}

    il['ants'] = insect.ants()
    il['dfly'] = insect.dfly()
    il['mosq'] = insect.mosq()
    il['worm'] = insect.worm()

    dic = { 'a1': il['ants']['title'],
            'a2': il['ants']['name'], 
            'a3': il['ants']['subtitle'],
            'a4': il['ants']['desc'], 
            'a5': il['ants']['label'], 
            'a6': il['ants']['icon'],
            'a7': il['ants']['preview'],
            'a8': il['ants']['slug'],
            'a9': il['ants']['step1'],
            'a10': il['ants']['diag1'], 
            'a11': il['ants']['step2'],
            'a12': il['ants']['diag2'], 
            'a13': il['ants']['step3'], 
            'a14': il['ants']['diag3'],
            #
            'b1': il['mosq']['title'], 
            'b2': il['mosq']['icon'],
            'b3': il['mosq']['slug'],
            'b1': il['mosq']['title'],
            # 
            'c1': il['dfly']['title'], 
            'c2': il['dfly']['icon'],
            'c3': il['dfly']['slug'],
            'c1': il['dfly']['title'],
            # 
            'd1': il['worm']['title'], 
            'd2': il['worm']['icon'],
            'd3': il['worm']['slug'],
            'd1': il['worm']['title'],
                }

    return render_template('details.html', insects=il, dic=dic) 


#e-bee  /  TLAL
@app.route('/tools/data_share')
def bees():
    insect = InsectData()
    il = {}

    il['bees'] = insect.bees()
    il['lbug'] = insect.lbug()
    il['bfly'] = insect.bfly()

    dic = { 'a1': il['bees']['title'],
            'a2': il['bees']['name'], 
            'a3': il['bees']['subtitle'],
            'a4': il['bees']['desc'], 
            'a5': il['bees']['label'], 
            'a6': il['bees']['icon'],
            'a7': il['bees']['preview'],
            'a8': il['bees']['slug'],
            'a9': il['bees']['step1'],
            'a10': il['bees']['diag1'], 
            'a11': il['bees']['step2'],
            'a12': il['bees']['diag2'], 
            'a13': il['bees']['step3'], 
            'a14': il['bees']['diag3'],
            #
            'b1': il['lbug']['title'], 
            'b2': il['lbug']['icon'],
            'b3': il['lbug']['slug'],
            'b1': il['lbug']['title'],
            # 
            'c1': il['bfly']['title'], 
            'c2': il['bfly']['icon'],
            'c3': il['bfly']['slug'],
            'c1': il['bfly']['title'],
                }

    return render_template('details.html', insects=il, dic=dic)  

#e-ladybug  /  MICA
@app.route('/tools/data_website')
def lbug():
    insect = InsectData()
    il = {}

    il['bees'] = insect.bees()
    il['lbug'] = insect.lbug()
    il['bfly'] = insect.bfly()

    dic = { 'a1': il['lbug']['title'],
            'a2': il['lbug']['name'], 
            'a3': il['lbug']['subtitle'],
            'a4': il['lbug']['desc'], 
            'a5': il['lbug']['label'], 
            'a6': il['lbug']['icon'],
            'a7': il['lbug']['preview'],
            'a8': il['lbug']['slug'],
            'a9': il['lbug']['step1'],
            'a10': il['lbug']['diag1'], 
            'a11': il['lbug']['step2'],
            'a12': il['lbug']['diag2'], 
            'a13': il['lbug']['step3'], 
            'a14': il['lbug']['diag3'],
            #
            'b1': il['bees']['title'], 
            'b2': il['bees']['icon'],
            'b3': il['bees']['slug'],
            # 
            'c1': il['bfly']['title'], 
            'c2': il['bfly']['icon'],
            'c3': il['bfly']['slug'],
                }

    return render_template('details.html', insects=il, dic=dic)    

#e-Butterfly   /   PAPA
@app.route('/tools/data_combinator')
def bfly():
    insect = InsectData()
    il = {}

    il['bees'] = insect.bees()
    il['lbug'] = insect.lbug()
    il['bfly'] = insect.bfly()

    dic = { 'a1': il['bfly']['title'],
            'a2': il['bfly']['name'], 
            'a3': il['bfly']['subtitle'],
            'a4': il['bfly']['desc'], 
            'a5': il['bfly']['label'], 
            'a6': il['bfly']['icon'],
            'a7': il['bfly']['preview'],
            'a8': il['bfly']['slug'],
            'a9': il['bfly']['step1'],
            'a10': il['bfly']['diag1'], 
            'a11': il['bfly']['step2'],
            'a12': il['bfly']['diag2'], 
            'a13': il['bfly']['step3'], 
            'a14': il['bfly']['diag3'],
            #
            'b1': il['lbug']['title'], 
            'b2': il['lbug']['icon'],
            'b3': il['lbug']['slug'],
            # 
            'c1': il['bees']['title'], 
            'c2': il['bees']['icon'],
            'c3': il['bees']['slug'],
                }

    return render_template('details.html', insects=il, dic=dic)       






@app.route('/pricing')
def prici():
    insect = InsectData()
    il = {}

    il['spid'] = insect.spid()
    il['cica'] = insect.cica()
    il['dfly'] = insect.dfly()
    il['mosq'] = insect.mosq()
    il['worm'] = insect.worm()
    il['bees'] = insect.bees()
    il['lbug'] = insect.lbug()
    il['bfly'] = insect.bfly()

    return render_template('pricing.html', insects=il) 


@app.route('/how')
def how():
    insect = InsectData()
    il = {}

    il['spid'] = insect.spid()
    il['cica'] = insect.cica()
    il['dfly'] = insect.dfly()
    il['mosq'] = insect.mosq()
    il['worm'] = insect.worm()
    il['bees'] = insect.bees()
    il['lbug'] = insect.lbug()
    il['bfly'] = insect.bfly()
    il['ants'] = insect.ants()

    dic = { 'a1': "",
            
          }

    return render_template('hiw.html', insects=il, dic=dic) 



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
