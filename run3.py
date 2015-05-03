from flask import Flask, request
from flask import render_template
from InsectData import InsectData
import smtplib
from config import FROMEMAIL, FROMPASS, TOEMAIL

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def hello():
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

    dic = { 'mes1': "0",}


    return render_template('landing.html', insects=il, dic=dic) 




@app.route("/business_facts", methods=["GET", "POST"])
#@login_required
def mbf_start():
    data = {}
    data['mask']= "mbf"
    data['title']= "Business Facts about your company"
    return render_template("/myring_biz/start.html", data=data)




@app.route("/business_profile", methods=["GET", "POST"])
#@login_required
def mbf_profile():
    data = {}
    data['mask']= "mbf"
    data['title']= "Business Profile with product and Services descriptions"
    return render_template("/myring_biz/profile.html", data=data)




@app.route("/faq", methods=["GET", "POST"])
#@login_required
def mbf_faq():
    data = {}
    data['mask']= "mbf"
    data['title']= "Frequent Asked Questions"
    return render_template("/myring_biz/faq.html", data=data)  



@app.route("/pricing", methods=["GET", "POST"])
#@login_required
def mbf_pricing():
    data = {}
    data['mask']= "mbf"
    data['title']= "Pricing"
    return render_template("/myring_biz/pricing.html", data=data)  
     


@app.route("/experts", methods=["GET", "POST"])
#@login_required
def mbf_experts():
    data = {}
    data['mask']= "mbf"
    data['title']= "Experts for hire"
    return render_template("/myring_biz/experts.html", data=data)  



@app.route("/developers", methods=["GET", "POST"])
#@login_required
def mbf_developers():
    data = {}
    data['mask']= "mbf"
    data['title']= "Integrate Business Facts"
    return render_template("/myring_biz/developers.html", data=data)  






# REPORTS    

@app.route("/facts/parkcentralny", methods=["GET", "POST"])
#@login_required
def r0002():
    data = {}
    data['mask']= "mbf"

    # HOTEL INFO
    
    data['Name']= "Park Central NY" 
    data['Address']= "870 Seventh Avenue at 56th Street"
    data['City']= "NewYork"
    data['State']= "NY"
    data['Zip']= "10018"
    data['Industry']= "10018"


    data['OneLine'] = [{
                #This USES THE FACTCARD MACRO
                #Title of the card
                'fc_SubTitle':'One Line Description',
                'fc_Descriptions': {
                    'en': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 
                    'sp': 'espanol del product 1', 
                    'fr': 'frances del product 1'
                    }
                }]# CLOSE

    data['Description'] = [{
            #This USES THE FACTCARD MACRO
            #Title of the card
            'fc_SubTitle':'One Line Description',
            'fc_Descriptions': {
                'en': 'ingles del product 1', 
                'sp': 'espanol del product 1', 
                'fr': 'frances del product 1'
                }
            }]# CLOSE



    #Contact
    data['Website']= "x14"
    data['Mail']= "x12"
    data['Phone']= "x13"
    data['Fax']= "x15"
    data['tollfree']= "x16"
    data['Newsletter']= "x18"
    data['Founded']= "x18"
    data['Closed']= "x18"

    #SocialMedia
        # twitter
    data['SM1']= "x19"
        # facebook
    data['SM2']= "x20"
        # youtube
    data['SM3']= "x21"
        # instagram
    data['SM4']= "x22"
     #External Links
    data['LINK1']= "x23"
    data['LINK2']= "x23"
    data['LINK3']= "x23"
    data['LINK4']= "x23"

    # DETAILS
    data['checkin']= "x06"
    data['checkout']= "x07"
    data['numberRooms']= "x08"
    data['resAge']= "x09"
    data['founded']= "x10"
    data['renovation']= "x11"
    data['payments']="x12"
    data['accesibility']="x12"
    data['rank']= "x06"
    data['closeby']= "x06"
    data['founded']= "x06"
    data['lastRenovation']= "x06"
    data['exited']= "x06"

    #StoryTelling
    data['History']= "x14"
    data['HistoryPhotos']= "x14"
    data['Facts']= "x14"
    data['OurStaff']= "x14"
    data['Awards']= "x14"
    data['FAQ']= "x14"
    data['FactualID']= "x14"



    data['history'] = [{
                    #This USES THE FACTCARD MACRO
                    #Title of the card
                    'fc_SubTitle':'History',
                    # Fields used:  History, History2, History3
                    'fc_Descriptions': {
                        'en': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi viverra tortor sit amet justo volutpat, et varius libero lobortis. Nullam mattis turpis quis nunc efficitur suscipit. Sed eu vestibulum nisl, quis finibus leo. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam hendrerit malesuada lacus. Nam nibh quam, convallis a neque at, commodo cursus tortor. Morbi mollis purus sem, vel dapibus augue ornare malesuada. Donec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestas', 
                        'sp': '', 
                        'fr': 'frances del product 1'
                        },
                    # This is the organization owner of the images
                    'fc_Owner':'teamamerica',
                    # photos ids
                    'fc_Photos': ['6896928037','3498992745','3579873745','3836044439'],
                    

                    }]# CLOSE

    data['staff'] = [{
                    'fc_Title':'Our Staff',
                    'fc_Descriptions': {
                        'en': 'ingles del product 1', 
                        'sp': 'espanol del product 1', 
                        'fr': 'frances del product 1'
                        },
                    'fc_Owner':'teamamerica',
                    'fc_Photos': ['6896928037','3498992745','3579873745','3836044439'],
                    'fc_Links': {
                            'r1': '', 
                            'r2': '',  
                            'r3': ''
                        }  
                    }]# CLOSE

    data['details'] = [{
                    'fc_SubTitle':'Details',
                    'fc_List': {
                            'd1': ['Check in','444'], 
                            'd2': ['Check out','555'],  
                            'd3': ['numberRooms','333'], 
                            'd4': ['Reservation Age','333'], 
                        }

                    }]# CLOSE

    data['contact'] = [{
                    'fc_SubTitle':'Contact',
                    'fc_List': {
                            'd1': ['Phone','444'], 
                            'd2': ['Fax','555'],  
                            'd3': ['Toll-free','333'], 
                            'd4': ['Sales','333'], 
                        }

                    }]# CLOSE


    data['curious'] = [{
                    'fc_SubTitle':'Curious Facts',
                    'fc_Specs': {
                            'd1': ['fact 1','Carpintero'], 
                            'd2': ['fact 2','Soldado'],  
                            'd3': ['fact 3','Musico'], 
                        },
                    }]# CLOSE







    data['Includes'] = [{
                    'fc_SubTitle':'Ammenities',

                    'fc_Tags':[{'name': 'Business', 
                                'list': ['a_001','a_002','a_003']
                                },
                                {'name': 'Beauty', 
                                'list': ['b_001','b_002','b_003']
                                },
                                {'name': 'Concierge', 
                                'list': ['c_001','c_002','c_003','c_004','c_005','c_006']
                                },
                                {'name': 'Food', 
                                'list': ['d_001','d_002','d_003','d_004','d_005','d_006','d_007','d_008']
                                },
                                {'name': 'Events', 
                                'list': ['e_001','e_002','e_003']
                                },
                                {'name': 'Fitness', 
                                'list': ['f_001','f_002','f_003','f_004','f_005']
                                },
                                {'name': 'Kids', 
                                'list': ['g_001','g_002','g_003','g_004']
                                },
                                {'name': 'Leisure', 
                                'list': ['h_001','h_002','h_003','h_004']
                                },
                                {'name': 'Medical', 
                                'list': ['i_001','i_002','i_003','i_004','i_005']
                                },
                                {'name': 'pets', 
                                'list': ['j_001','j_002','j_003','j_004']
                                },
                                {'name': 'Pool', 
                                'list': ['k_001','k_002','k_003','k_004','k_005']
                                },
                                {'name': 'Shopping', 
                                'list': ['l_001','l_002','l_003','l_004','l_005']
                                },
                                {'name': 'Smoking', 
                                'list': ['m_001','m_002','m_003']
                                },
                                {'name': 'Transportation', 
                                'list': ['n_001','n_002','n_003','n_004','n_005']
                                },
                            ]

                    }]# CLOSE



    # HOTEL SPECIFICATIONS

    # data['productRoom'] = [{'name': 'Single Room', 
    #                         'category': 'SGL Room / Luxury', 
    #                         'avgsize':'300', 
    #                         'smoking': 'No', 
    #                         'ammen': ['d_001', 'a_001', 'b_002'],
    #                         'photos': ['6896928037','3498992745','3579873745','3836044439','5871936148'],
    #                         'descriptions': {
    #                             'en': 'ingles del product 1', 
    #                             'sp': 'espanol del product 1', 
    #                             'fr': 'frances del product 1'
    #                             }
    #                         },
    #                         {'name': 'Double Room', 
    #                         'category': 'SGL Room / Luxury', 
    #                         'avgsize':'300', 
    #                         'smoking': 'No', 
    #                         'ammen': ['d_001', 'a_001', 'b_002'],
    #                         'photos': ['6896928037','3498992745','3579873745','3836044439','5871936148'],
    #                         'descriptions': {
    #                             'en': 'ingles del product 2', 
    #                             'sp': 'espanol del product 2', 
    #                             'fr': 'frances del product 2'
    #                             }
    #                         }

    #                     ]

    # data['productService'] = [{'name': 'El Tropicaloso', 
    #                         'type': 'Dinning Cruise', 
    #                         'sameAddress':'',
    #                         'alt_address':'',
    #                         'alt_city':'',
    #                         'alt_state':'',
    #                         'alt_zip':'', 
    #                         'duration':'',
    #                         'minAge': '18', 
    #                         'minPax': '18', 
    #                         'attire': 'Casual', 
    #                         'accesibility': ['Wheelchair'],
    #                         'languages':['6896928037','3498992745','3579873745','3836044439','5871936148'], 
    #                         'photos': ['6896928037','3498992745','3579873745','3836044439','5871936148'],
    #                         'lineDescription': {
    #                             'en': 'ingles del product 1', 
    #                             'sp': 'espanol del product 1', 
    #                             'fr': 'frances del product 1'
    #                             },
    #                         'Description': {
    #                             'en': 'ingles del product 1', 
    #                             'sp': 'espanol del product 1', 
    #                             'fr': 'frances del product 1'
    #                             },
    #                         'facts': {
    #                         'd1': ['fact1','444'], 
    #                         'd2': ['fact2','555'],  
    #                         'd3': ['fact3','333'], 
    #                         'd4': ['fact4','333'], 
    #                         }, 
    #                         'notes':'notes about the service', 
    #                         'carParking':'',
    #                         'busParking':'',
    #                         'privateParty':'',
    #                         'freeSell':'',
    #                         'blackOutDates':'',
    #                         'cancellationPolicy':'',
    #                         'schedule': {
    #                             'd1': ['Monday','14:00','21:00'], 
    #                             'd2': ['Tuesday','10:00','21:00'],  
    #                             'd3': ['Wednesday','10:00','21:00'], 
    #                             'd4': ['Thursday','10:00','21:00'], 
    #                             'd5': ['Friday','10:00','21:00'], 
    #                             'd6': ['Saturday','11:00','19:00'], 
    #                             'd7': ['Sunday','11:00','19:00'], 
    #                             },
    #                         'alt_Twitter':'',
    #                         'alt_facebook':'',
    #                         'alt_Instagram':'',
    #                         'alt_YouTube':'',
    #                         },
    #                         {'name': 'El Otelo', 
    #                         'type': 'Dinning Cruise', 
    #                         'sameAddress':'',
    #                         'alt_address':'',
    #                         'alt_city':'',
    #                         'alt_state':'',
    #                         'alt_zip':'', 
    #                         'duration':'',
    #                         'minAge': '18', 
    #                         'minPax': '18', 
    #                         'attire': 'Casual', 
    #                         'accesibility': ['Wheelchair'],
    #                         'languages':['6896928037','3498992745','3579873745','3836044439','5871936148'], 
    #                         'photos': ['6896928037','3498992745','3579873745','3836044439','5871936148'],
    #                         'lineDescription': {
    #                             'en': 'ingles del product 1', 
    #                             'sp': 'espanol del product 1', 
    #                             'fr': 'frances del product 1'
    #                             },
    #                         'Description': {
    #                             'en': 'ingles del product 1', 
    #                             'sp': 'espanol del product 1', 
    #                             'fr': 'frances del product 1'
    #                             },
    #                         'facts': {
    #                         'd1': ['fact1','444'], 
    #                         'd2': ['fact2','555'],  
    #                         'd3': ['fact3','333'], 
    #                         'd4': ['fact4','333'], 
    #                         }, 
    #                         'notes':'notes about the service', 
    #                         'carParking':'',
    #                         'busParking':'',
    #                         'privateParty':'',
    #                         'freeSell':'',
    #                         'blackOutDates':'',
    #                         'cancellationPolicy':'',
    #                         'schedule': {
    #                             'd1': ['Monday','14:00','21:00'], 
    #                             'd2': ['Tuesday','10:00','21:00'],  
    #                             'd3': ['Wednesday','10:00','21:00'], 
    #                             'd4': ['Thursday','10:00','21:00'], 
    #                             'd5': ['Friday','10:00','21:00'], 
    #                             'd6': ['Saturday','11:00','19:00'], 
    #                             'd7': ['Sunday','11:00','19:00'], 
    #                             },
    #                         'alt_Twitter':'',
    #                         'alt_facebook':'',
    #                         'alt_Instagram':'',
    #                         'alt_YouTube':'',
    #                         },
    #                     ]


    



    
    data['staff'] = [{
                    'fc_SubTitle':'Our Staff',
                    'fc_Descriptions': {
                        'en': 'ingles del product 1', 
                        'sp': 'espanol del product 1', 
                        'fr': 'frances del product 1'
                        },
                    'fc_Owner':'teamamerica',
                    'fc_Photos': ['6896928037','3498992745','3579873745','3836044439'],

                    }]# CLOSE

    data['details'] = [{
                    'subTitle':'Details',
                    'lista': {
                            'd1': ['Check in','444'], 
                            'd2': ['Check out','555'],  
                            'd3': ['numberRooms','333'], 
                            'd4': ['Reservation Age','333'], 
                        }

                    }]# CLOSE

    data['contact'] = [{
                    'fc_SubTitle':'Contact',
                    'fc_List': {
                            'd1': ['Phone','444'], 
                            'd2': ['Fax','555'],  
                            'd3': ['Toll-free','333'], 
                            'd4': ['Sales','333'], 
                        }

                    }]# CLOSE


    data['curious'] = [{
                    'fc_SubTitle':'Curious Facts',
                    'fc_Specs': {
                            'd1': ['fact 1','Carpintero'], 
                            'd2': ['fact 2','Soldado'],  
                            'd3': ['fact 3','Musico'], 
                        },
                    }]# CLOSE


    data['photos'] = [{
                    
                    'fc_Owner':'teamamerica',
                    'fc_Photos': ['6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439'],

                    }]# CLOSE



 
    data['fc_template'] = [{
                    'fc_Title':'This is the Title',
                    'fc_SubTitle':'And this is the subtitle',
                    'fc_Specs': {
                            'd1': ['spec1','10 of this'], 
                            'd2': ['spec2','50 of that'],  
                            'd3': ['spec3','40 of this ot ipsum lorem and the otherher'], 
                        },
                    'fc_Descriptions': {
                        'en': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi viverra tortor sit amet justo volutpat, et varius libero lobortis. Nullam mattis turpis quis nunc efficitur suscipit. Sed eu vestibulum nisl, quis finibus leo. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam hendrerit malesuada lacus. Nam nibh quam, convallis a neque at, commodo cursus tortor. Morbi mollis purus sem, vel dapibus augue ornare malesuada. Donec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestas', 
                        'sp': '', 
                        'fr': 'frances del product 1'
                        },
                    'fc_Owner':'teamamerica',
                    'fc_Photos': ['6896928037','3498992745','3579873745','3836044439'],
                    'fc_Links': {
                            'd1': ['Link1 Name','http://www.myring.io'], 
                            'd2': ['Link2 Name','http://www.myring.io'],  
                            'd3': ['Link3 Name','http://www.myring.io'], 
                        },
                    'fc_Tags':[{'name': 'Business', 
                                'list': ['a_001','a_002','a_003']
                                },
                                {'name': 'Beauty', 
                                'list': ['b_001','b_002','b_003']
                                },
                                {'name': 'Concierge', 
                                'list': ['c_001','c_002','c_003','c_004','c_005','c_006']
                                },
                                {'name': 'Food', 
                                'list': ['d_001','d_002','d_003','d_004','d_005','d_006','d_007','d_008']
                                },
                                {'name': 'Events', 
                                'list': ['e_001','e_002','e_003']
                                },
                                {'name': 'Fitness', 
                                'list': ['f_001','f_002','f_003','f_004','f_005']
                                },
                                {'name': 'Kids', 
                                'list': ['g_001','g_002','g_003','g_004']
                                },
                                {'name': 'Leisure', 
                                'list': ['h_001','h_002','h_003','h_004']
                                },
                                {'name': 'Medical', 
                                'list': ['i_001','i_002','i_003','i_004','i_005']
                                },
                                {'name': 'pets', 
                                'list': ['j_001','j_002','j_003','j_004']
                                },
                                {'name': 'Pool', 
                                'list': ['k_001','k_002','k_003','k_004','k_005']
                                },
                                {'name': 'Shopping', 
                                'list': ['l_001','l_002','l_003','l_004','l_005']
                                },
                                {'name': 'Smoking', 
                                'list': ['m_001','m_002','m_003']
                                },
                                {'name': 'Transportation', 
                                'list': ['n_001','n_002','n_003','n_004','n_005']
                                },
                            ],

                    'fc_Schedule': {
                            'd1': ['Monday','14:00','21:00'], 
                            'd2': ['Tuesday','10:00','21:00'],  
                            'd3': ['Wednesday','10:00','21:00'], 
                            'd4': ['Thursday','10:00','21:00'], 
                            'd5': ['Friday','10:00','21:00'], 
                            'd6': ['Saturday','11:00','19:00'], 
                            'd7': ['Sunday','11:00','19:00'], 
                            },  
                    'fc_List': {
                            'd1': ['Phone','444'], 
                            'd2': ['Fax','555'],  
                            'd3': ['Toll-free','333'], 
                            'd4': ['Sales','333'], 
                        },
                    'fc_SmallNotes': {
                            'd1': ['Notes','Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam hendrerit malesuada lacus.'], 
                            'd2': ['Cancellation Policy','Donec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestasDonec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestasDonec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestasDonec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestas']
                        },

                    }]# CLOSE


    data['Services'] = [{
                    'fc_Title':'Bateaux New York',
                    'fc_SubTitle':'The best way to see the city , unique Brunch',
                    'fc_Category':'Cruise Waterfront',
                    'fc_Specs': {
                            'd1': ['Category','Dinning Cruise'], 
                            'd2': ['Minimum Booking Age','18'],  
                            'd3': ['Attire','Casual'], 
                        },
                    'fc_Descriptions': {
                        'en': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi viverra tortor sit amet justo volutpat, et varius libero lobortis. Nullam mattis turpis quis nunc efficitur suscipit. Sed eu vestibulum nisl, quis finibus leo. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam hendrerit malesuada lacus. Nam nibh quam, convallis a neque at, commodo cursus tortor. Morbi mollis purus sem, vel dapibus augue ornare malesuada. Donec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestas', 
                        'sp': '', 
                        'fr': 'frances del product 1'
                        },
                    'fc_Owner':'teamamerica',
                    'fc_Photos': ['6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439'],
                    'fc_Links': {
                            'd1': ['Website','http://www.myring.io'], 
                            'd2': ['NewYork TImes','http://www.myring.io'],  
                            'd3': ['TimeOut','http://www.myring.io'], 
                        },
                    'fc_Tags':[{'name': 'Business', 
                                'list': ['a_001','a_002','a_003']
                                },
                                {'name': 'Beauty', 
                                'list': ['b_001','b_002','b_003']
                                }
                                
                            ],

                    'fc_Schedule': {
                            'd1': ['Monday','14:00','21:00'], 
                            'd2': ['Tuesday','10:00','21:00'],  
                            'd3': ['Wednesday','10:00','21:00'], 
                            'd4': ['Thursday','10:00','21:00'], 
                            'd5': ['Friday','10:00','21:00'], 
                            'd6': ['Saturday','11:00','19:00'], 
                            'd7': ['Sunday','11:00','19:00'], 
                            },  
                    'fc_List': {
                            'd1': ['Phone','444'], 
                            'd2': ['Fax','555'],  
                            'd3': ['Toll-free','333'], 
                            'd4': ['Sales','333'], 
                        },
                        'fc_SmallNotes': {
                            'd1': ['Notes','Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam hendrerit malesuada lacus.'], 
                            'd2': ['Cancellation Policy','Donec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestasDonec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestasDonec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestasDonec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestas']
                        },

                    },
                    # SECOND ITEM
                    {
                    'fc_Title':'La Pecorina',
                    'fc_SubTitle':'The best Brger in Town and unique familiar mood',
                    'fc_Specs': {
                            'd1': ['Category','Dinning Cruise'], 
                            'd2': ['Minimum Booking Age','18'],  
                            'd3': ['Attire','Casual'], 
                        },
                    'fc_Descriptions': {
                        'en': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi viverra tortor sit amet justo volutpat, et varius libero lobortis. Nullam mattis turpis quis nunc efficitur suscipit. Sed eu vestibulum nisl, quis finibus leo. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam hendrerit malesuada lacus. Nam nibh quam, convallis a neque at, commodo cursus tortor. Morbi mollis purus sem, vel dapibus augue ornare malesuada. Donec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestas', 
                        'sp': '', 
                        'fr': 'frances del product 1'
                        },
                    'fc_Owner':'teamamerica',
                    'fc_Photos': ['6896928037','3498992745','3579873745','3836044439'],
                    'fc_Links': {
                            'd1': ['Website','http://www.myring.io'], 
                            'd2': ['NewYork TImes','http://www.myring.io'],  
                            'd3': ['TimeOut','http://www.myring.io'], 
                        },
                    'fc_Tags':[{'name': 'Business', 
                                'list': ['a_001','a_002','a_003']
                                },
                                {'name': 'Beauty', 
                                'list': ['b_001','b_002','b_003']
                                }
                                
                            ],

                    'fc_Schedule': {
                            'd1': ['Monday','14:00','21:00'], 
                            'd2': ['Tuesday','10:00','21:00'],  
                            'd3': ['Wednesday','10:00','21:00'], 
                            'd4': ['Thursday','10:00','21:00'], 
                            'd5': ['Friday','10:00','21:00'], 
                            'd6': ['Saturday','11:00','19:00'], 
                            'd7': ['Sunday','11:00','19:00'], 
                            },  
                    'fc_List': {
                            'd1': ['Phone','444'], 
                            'd2': ['Fax','555'],  
                            'd3': ['Toll-free','333'], 
                            'd4': ['Sales','333'], 
                        },
                        'fc_SmallNotes': {
                            'd1': ['Cancellation Policy','Donec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestasDonec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestasDonec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestasDonec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestas'], 
                            'd2': ['Notes','Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam hendrerit malesuada lacus.']
                        },

                    }] # CLOSE



    data['Rooms'] = [{
                    'fc_Title':'Single Room Presidential',
                    'fc_Category':'Room',
                    'fc_Specs': {
                            'd1': ['Category','SGL Room'], 
                            'd2': ['Avg Size','300 sq ft.'],  
                            'd3': ['Smoking','No'], 
                        },
                    'fc_Descriptions': {
                        'en': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi viverra tortor sit amet justo volutpat, et varius libero lobortis. Nullam mattis turpis quis nunc efficitur suscipit. Sed eu vestibulum nisl, quis finibus leo. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam hendrerit malesuada lacus. Nam nibh quam, convallis a neque at, commodo cursus tortor. Morbi mollis purus sem, vel dapibus augue ornare malesuada. Donec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestas', 
                        'sp': '', 
                        'fr': 'frances del product 1'
                        },
                    'fc_Owner':'teamamerica',
                    'fc_Photos': ['6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439'],
                    'fc_Links': {
                            'd1': ['Website','http://www.myring.io'], 
                            'd2': ['NewYork TImes','http://www.myring.io'],  
                            'd3': ['TimeOut','http://www.myring.io'], 
                        },
                    'fc_Tags':[{'name': 'Business', 
                                'list': ['a_001','a_002','a_003']
                                },
                                {'name': 'Beauty', 
                                'list': ['b_001','b_002','b_003']
                                }
                                
                            ],


                        'fc_SmallNotes': {
                            'd1': ['Notes','Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam hendrerit malesuada lacus.'], 
                            'd2': ['Cancellation Policy','Donec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestasDonec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestasDonec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestasDonec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestas']
                        },
                        'fc_Tags':[{'name': 'Room Ammenities', 
                                'list': ['a_001','a_002','a_003']
                                }
                            ],

                    },

                    ]# CLOSE






    return render_template("/report/r0002.html", data=data)  




@app.route("/facts/ecruises", methods=["GET", "POST"])
#@login_required
def r0004():
    data = {}
    data['mask']= "mbf"

# HOTEL INFO
    data['id']= 7824441979
    data['org']='teamamerica'

    data['title']= "Entertainment Cruises NY" 
    data['name']= "Entertainment Cruises NY"
    data['address']= "Pier 62, Chelsea Piers, Suite 200"
    data['city']= "NewYork"
    data['state']= "NY"
    data['zip']= "10011"
        # Details
    data['checkin']= "16:00"
    data['checkout']= "12:00"
    data['rooms']= "935"
    data['resAge']= "21"
    data['founded']= "1924"
    data['renovation']= "2013"
        #Contact
    data['mail']= "Cruise.NewYork@entertainmentcruises.com"
    data['phone']= "866-433-9283"
    data['website']= "http://www.entertainmentcruises.com/our-cities/new-york"
    data['fax']= ""
    data['tollfree']= ""
    data['sales']= "Cruise.NewYork@entertainmentcruises.com"
    data['newsletter']= ""
        #Social
    data['twitter']= "ecnewyork "
    data['facebook']= ""
    data['youtube']= ""
    data['plus']= ""
    data['instagram']= "ecnewyork"


    





    return render_template("/report/r0004.html", data=data)  









# OLD


@app.route('/thankyou',methods=['GET', 'POST'])
def thankyou():
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
    dic = { 'mes1': "1",}

    if request.form['name'] and request.form['email']:

        print("Beta tester: "+request.form['name'] +"<"+request.form['email']+"> ")

        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()

        #Next, log in to the server
        server.login(FROMEMAIL, FROMPASS)

        #Send the mail
        msg = "\r\n".join([
          "From:"+FROMEMAIL,
          "To: ",
          "Subject: "+request.form['name'] +"<"+request.form['email']+"> Just subscribed to the Beta!",
          "",
          "Llame ahora! "+request.form['name'] +"<"+request.form['email']+">"
          ])
        #msg = "\nHello!" # The /n separates the message from the headers
        server.sendmail(FROMEMAIL, TOEMAIL, msg)
        server.quit()

        print("Email to "+request.form['email']+" sent succesfully ")

        return render_template('datasuite/home.html' , insects=il, dic=dic)
    else:
        return render_template('datasuite/home.html', insects=il, dic=dic) 


@app.route('/solutions')
def sol():
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
            'header': "big",

                }

    return render_template('datasuite/solutions.html', insects=il, dic=dic) 

@app.route('/solutions/model')
def solmod():

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

    dic = { 'a1': il['cica']['title'],
            'a2': il['cica']['name'], 
            'a3': il['cica']['subtitle'],
            'a4': il['cica']['desc'], 
            'a5': il['cica']['label'], 
            'a6': il['cica']['icon'],
            'a7': il['cica']['preview'],
            'a8': il['cica']['slug'],

            'b1': il['spid']['title'],
            'b2': il['spid']['name'], 
            'b3': il['spid']['subtitle'],
            'b4': il['spid']['desc'], 
            'b5': il['spid']['label'], 
            'b6': il['spid']['icon'],
            'b7': il['spid']['preview'],
            'b8': il['spid']['slug'],
                }

    return render_template('datasuite/solutions.html', insects=il, dic=dic) 
    

@app.route('/solutions/capture')
def solcap():

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

    return render_template('datasuite/solutions.html', insects=il, dic=dic) 


@app.route('/solutions/share')
def solsha():
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

    return render_template('datasuite/solutions.html', insects=il, dic=dic)        

# TOOOOOOLLLLLLSSSSSSSSTOOOOOOLLLLLLSSSSSSSS 

#m-arana / TOCA
@app.route('/tools/schema_modeler') 
def spid():
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
            'a15': il['spid']['details'],
            #
            'b1': il['cica']['title'], 
            'b2': il['cica']['icon'],
            'b3': il['cica']['slug'],
                }

    return render_template('datasuite/details.html', insects=il, dic=dic)  

#m-cicada  /  CHIQ
@app.route('/tools/semantic_labeler')
def cica():
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

    dic = { 'a1': il['cica']['title'],
            'a2': il['cica']['name'], 
            'a3': il['cica']['subtitle'],
            'a4': il['cica']['desc'], 
            'a5': il['cica']['label'], 
            'a6': il['cica']['icon'],
            'a7': il['cica']['preview'],
            'a8': il['cica']['slug'],
            'a9': il['cica']['step1'],
            'a10': il['cica']['diag1'], 
            'a11': il['cica']['step2'],
            'a12': il['cica']['diag2'], 
            'a13': il['cica']['step3'], 
            'a14': il['cica']['diag3'],
            'a15': il['cica']['details'],
            #
            'b1': il['spid']['title'], 
            'b2': il['spid']['icon'],
            'b3': il['spid']['slug'],
                }

    return render_template('datasuite/details.html', insects=il, dic=dic) 

#c-avispa  /  ETZA
@app.route('/tools/manual_capture')
def dfly():
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
            'a15': il['dfly']['details'],
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

    return render_template('datasuite/details.html', insects=il, dic=dic)  

#c-mosquitoe   /  APIP
@app.route('/tools/automatic_capture')
def mosq():
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
            'a15': il['mosq']['details'],
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

    return render_template('datasuite/details.html', insects=il, dic=dic)  


#c-worm   /  TEMO
@app.route('/tools/legacy_data')
def worm():
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
            'a15': il['worm']['details'],
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

    return render_template('datasuite/details.html', insects=il, dic=dic) 

#c-ant   /  TEMO
@app.route('/tools/data_scrapper')
def ants():
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
            'a15': il['ants']['details'],
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

    return render_template('datasuite/details.html', insects=il, dic=dic) 


#e-bee  /  TLAL
@app.route('/tools/data_share')
def bees():
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
            'a15': il['bees']['details'],
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

    return render_template('datasuite/details.html', insects=il, dic=dic)  

#e-ladybug  /  MICA
@app.route('/tools/data_website')
def lbug():
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
            'a15': il['lbug']['details'],
            #
            'b1': il['bees']['title'], 
            'b2': il['bees']['icon'],
            'b3': il['bees']['slug'],
            # 
            'c1': il['bfly']['title'], 
            'c2': il['bfly']['icon'],
            'c3': il['bfly']['slug'],
                }

    return render_template('datasuite/details.html', insects=il, dic=dic)    

#e-Butterfly   /   PAPA
@app.route('/tools/data_combinator')
def bfly():
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
            'a15': il['bfly']['details'],
            #
            'b1': il['lbug']['title'], 
            'b2': il['lbug']['icon'],
            'b3': il['lbug']['slug'],
            # 
            'c1': il['bees']['title'], 
            'c2': il['bees']['icon'],
            'c3': il['bees']['slug'],
                }

    return render_template('datasuite/details.html', insects=il, dic=dic)       



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
    il['ants'] = insect.ants()

    return render_template('datasuite/pricing.html', insects=il) 


@app.route('/faq')
def faq():

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

    return render_template('datasuite/faq1.html', insects=il, dic=dic) 


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

    return render_template('datasuite/hiw.html', insects=il, dic=dic) 


@app.route('/ecosystem')
def ecosystem():
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

    return render_template('datasuite/ecosystem.html', insects=il, dic=dic)     


@app.route('/templates')
def templates():
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

    return render_template('sandbox/templates.html', insects=il, dic=dic)    


@app.route('/blueprints')
def blueprints():
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

    return render_template('datasuite/blueprints.html', insects=il, dic=dic) 



@app.route('/autopitch')
def autopitch():
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

    return render_template('sandbox/autopitch.html', insects=il, dic=dic) 

# WIZARDS

@app.route('/wiz01')
def wiz01():
    return render_template('sandbox/wiz01.html')
     
@app.route('/wiz02')
def wiz02():
    return render_template('sandbox/wiz02.html') 

@app.route('/wiz03')
def wiz03():
    return render_template('sandbox/wiz03.html') 

@app.route('/wiz04')
def wiz04():
    return render_template('sandbox/wiz04.html')         



@app.route('/docs')
def docs():
    title = 'Documentation'
    return render_template('datasuite/docs.html', title=title) 




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
    return render_template('sandbox/avispa.html', name=name)

if __name__ == '__main__':
    app.run()
