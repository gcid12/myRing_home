from flask import Flask, request
from flask import render_template
from InsectData import InsectData
import smtplib
from config import FROMEMAIL, FROMPASS, TOEMAIL

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def hello():
    data = {}
    data['mask']= "mbf"
    data['title']= "Data Communities"


    return render_template('/landing.html', data=data) 




@app.route("/business_facts", methods=["GET", "POST"])
#@login_required
def mbf_start():
    data = {}
    data['mask']= "mbf"
    data['title']= "Business Facts about your company"
    return render_template("/myring_biz/start.html", data=data)


@app.route("/why", methods=["GET", "POST"])
#@login_required
def mbf_why():
    data = {}
    data['mask']= "mbf"
    data['title']= "Why Now"
    return render_template("/myring_biz/why.html", data=data)



@app.route("/business_profile", methods=["GET", "POST"])
#@login_required
def mbf_profile():
    data = {}
    data['mask']= "mbf"
    data['title']= "Business Facts"
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
    data['title']= "Developers"
    return render_template("/myring_biz/developers.html", data=data)  



@app.route("/ecosystem", methods=["GET", "POST"])
#@login_required
def mbf_ecosystem():
    data = {}
    data['mask']= "mbf"
    data['title']= "ecosystem"
    return render_template("/myring_biz/why.html", data=data)




# REPORTS    

@app.route("/facts/travelservice", methods=["GET", "POST"])
#@login_required
def travelservice():

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

    #CONTACT
    data['Website']= "x14"
    data['Mail']= "x12"
    data['Phone']= "x13"
    data['Fax']= "x15"
    data['Newsletter']= "x18"

    #DETAILS
    data['Founded']= "x18"
    data['Closed']= "x18"
    data['ResAge']= "x09"
    data['Founded']= "x10"
    data['payments']="x12"


    #SOCIALMEDIA
        # twitter
    data['SM1']= "x19"
        # facebook
    data['SM2']= "x20"
        # youtube
    data['SM3']= "x21"
        # instagram
    data['SM4']= "x22"
        #Other Links
    data['LINK1']= "x23"
    data['LINK2']= "x23"
    data['LINK3']= "x23"
    data['LINK4']= "x23"


    #HISTORY
    data['Facts']= "x14"
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
                    # HISTORY PHOTOS
                    'fc_Owner':'teamamerica',
                    # PHOTOS
                    'fc_Photos': ['6896928037','3498992745','3579873745','3836044439'],
                    

                    }]# CLOSE
    data['OurStaff'] = [{
                    'fc_Title':'Our Staff',
                    'fc_Descriptions': {
                        'en': 'ingles del product 1', 
                        'sp': 'espanol del product 1', 
                        'fr': 'frances del product 1'
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

    data['contact'] = [{
                    'fc_SubTitle':'Contact',
                    'fc_List': {
                            'd1': ['Phone','444'], 
                            'd2': ['Fax','555'],  
                            'd3': ['Toll-free','333'], 
                            'd4': ['Sales','333'], 
                        }

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

    data['photos'] = [{
                    
                    'fc_Owner':'teamamerica',
                    'fc_Photos': ['6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439'],

                    }]# CLOSE
                    
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

    # HOTEL////HOTEL////HOTEL////HOTEL////HOTEL////HOTEL////HOTEL////
    # HOTEL////HOTEL////HOTEL////HOTEL////HOTEL////HOTEL////HOTEL////

    # DETAILS ONLY HOTEL
    data['Checkin']= "x06" 
    data['Checkout']= "x07"
    data['NumberRooms']= "x08"
    data['Parking']= "x08"
    data['Accesibility']="x12"
    data['Rank']= "x06"
    data['LastRenovation']= "x06"

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

    # HOTEL AMMENITIES
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
                            ],
                            }]


    return render_template("/sandbox/factcard.html", data=data)   

@app.route("/facts/parkcentral", methods=["GET", "POST"])
#@login_required
def facts_001():

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
                'fc_SubTitle':'Full Description',
                'fc_DescriptionsSize':'1',
                'fc_Descriptions': {
                      'd1': ['en',1 ,'Midtown convenience. Classic hospitality. Complete comfort. A celebrated past. It all comes together at the Park Central New York Hotel. located squarely amidst New York`s most popular sights and hotels in Midtown Manhattan. Our mix of exciting amenities pay homage to our glamorous past, while presenting a modern spin on the hotel`s electrifying environment. Guests will delight in escaping the hectic city life to bask in the stylish Park Central New York.'], 
                      'd2': ['sp',1,'Conveniencia Midtown . Hospitalidad Classic. Total comodidad . Un pasado celebre . Todo confluye en el Hotel Parque Central de Nueva York. situado de lleno en medio de nuevas Yorks atracciones turisticas mas populares y hoteles en el centro de Manhattan . Nuestra mezcla de comodidades sorprendentes rendir homenaje a nuestro pasado glamoroso , al tiempo que presenta un giro moderno en el medio ambiente electrizante del hotel. Los huespedes se deleitaran con escapar del bullicio de la ciudad para tomar el sol en el elegante Parque Central de Nueva York.'],  
                      'd3': ['fr',4,'(not defined)'], 
                  }
                }]# CLOSE

    data['Description'] = [{
            #This USES THE FACTCARD MACRO
            #Title of the card
            'fc_SubTitle':'One Line Description',
            'fc_DescriptionsSize':'2',
            'fc_Descriptions': {
                    'd1': ['en',1 ,'The midtown new york city hotel Central to new york`s best'], 
                    'd2': ['sp',1,'El hotel mejor situado en Midtown Manhattan, cerca de lo mejor de NewYork'],  
                    'd3': ['fr',4,'(not defined)'], 
                }

            }]# CLOSE

    #CONTACT
    data['Website']= "x14"
    data['Mail']= "x12"
    data['Phone']= "x13"
    data['Fax']= "x15"
    data['Newsletter']= "x18"

    #DETAILS
    data['Founded']= "x18"
    data['Closed']= "x18"
    data['ResAge']= "x09"
    data['Founded']= "x10"
    data['payments']="x12"


    #SOCIALMEDIA
        # twitter
    data['SM1']= "x19"
        # facebook
    data['SM2']= "x20"
        # youtube
    data['SM3']= "x21"
        # instagram
    data['SM4']= "x22"
        #Other Links
    data['LINK1']= "x23"
    data['LINK2']= "x23"
    data['LINK3']= "x23"
    data['LINK4']= "x23"


    #HISTORY
    data['Facts']= "x14"
    data['Awards']= "x14"
    data['FAQ']= "x14"
    data['FactualID']= "x14"
    data['history'] = [{
                    #This USES THE FACTCARD MACRO
                    #Title of the card
                    'fc_SubTitle':'History',
                    # Fields used:  History, History2, History3
                    'fc_Descriptions': {
                      'd1': ['en',1 ,'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi viverra tortor sit amet justo volutpat, et varius libero lobortis. Nullam mattis turpis quis nunc efficitur suscipit. Sed eu vestibulum nisl, quis finibus leo. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam hendrerit malesuada lacus. Nam nibh quam, convallis a neque at, commodo cursus tortor. Morbi mollis purus sem, vel dapibus augue ornare malesuada. Donec id pulvinar enim. Praesent finibus nibh ac sapien ultrices egestas'], 
                      'd2': ['sp',4,'(not defined)'],  
                      'd3': ['fr',4,'(not defined)'], 
                    },
                    # HISTORY PHOTOS
                    'fc_Owner':'teamamerica',
                    # PHOTOS
                    'fc_Photos': ['6896928037','3498992745','3579873745','3836044439'],
                    

                    }]# CLOSE
    data['OurStaff'] = [{
                    'fc_Title':'Our Staff',
                    'fc_Descriptions': {
                      'd1': ['en',4 ,'(not defined)'], 
                      'd2': ['sp',4,'(not defined)'],  
                      'd3': ['fr',4,'(not defined)'], 
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

    data['contact'] = [{
                    'fc_SubTitle':'Contact',
                    'fc_List': {
                            'd1': ['Phone','444'], 
                            'd2': ['Fax','555'],  
                            'd3': ['Toll-free','333'], 
                            'd4': ['Sales','333'], 
                        }

                    }]# CLOSE

    data['photos'] = [{
                    
                    'fc_Owner':'teamamerica',
                    'fc_Photos': ['6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439'],
                    'fc_SmartPhotos': {
                            'p1': [1,'6896928037','ok'], 
                            'p2': [2,'3498992745','ok'],  
                            'p3': [3,'3836044439','ok'], 
                            'p4': [4,'6896928037','ok'], 
                        }

                    }]# CLOSE
                    
    data['staff'] = [{
                    'fc_SubTitle':'Our Staff',
                    'fc_Descriptions': {
                      'd1': ['en',4 ,'(not defined)'], 
                      'd2': ['sp',4,'(not defined)'],  
                      'd3': ['fr',4,'(not defined)'], 
                      },
                    'fc_Owner':'teamamerica',
                    'fc_Photos': ['6896928037','3498992745','3579873745','3836044439'],
                    'fc_SmartPhotos': {
                            'p1': [1,'6896928037','ok'], 
                            'p2': [2,'3498992745','ok'],  
                            'p3': [3,'3836044439','ok'], 
                            'p4': [4,'6896928037','ok'], 
                        }


                    }]# CLOSE

    # HOTEL////HOTEL////HOTEL////HOTEL////HOTEL////HOTEL////HOTEL////
    # HOTEL////HOTEL////HOTEL////HOTEL////HOTEL////HOTEL////HOTEL////

    # DETAILS ONLY HOTEL
    data['Checkin']= "x06" 
    data['Checkout']= "x07"
    data['NumberRooms']= "x08"
    data['Parking']= "x08"
    data['Accesibility']="x12"
    data['Rank']= "x06"
    data['LastRenovation']= "x06"

    data['Rooms'] = [{
                    'fc_Title':'Single Room Presidential',
                    'fc_Category':'Room',
                    'fc_Specs': {
                            'd1': ['Category','SGL Room'], 
                            'd2': ['Avg Size','300 sq ft.'],  
                            'd3': ['Smoking','No'], 
                        },
                    'fc_Descriptions': {
                      'd1': ['en',4 ,'(not defined)'], 
                      'd2': ['sp',4,'(not defined)'],  
                      'd3': ['fr',4,'(not defined)'], 
                      },
                    'fc_Owner':'teamamerica',
                    'fc_Photos': ['6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439','6896928037','3498992745','3579873745','3836044439'],
                    'fc_SmartPhotos': {
                            'p1': [1,'6896928037','ok'], 
                            'p2': [2,'3498992745','ok'],  
                            'p3': [3,'3836044439','ok'], 
                            'p4': [4,'6896928037','ok'], 
                        },
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

    # HOTEL AMMENITIES
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
                            ],
                            }]


    return render_template("/sandbox/factcard.html", data=data)  


@app.route('/facts/ecruises/<showme>')
#@login_required
def facts_002(showme):

    data = {}
    data['mask']= "mbf"
    data['mode']= showme
    data['slug']= "ecruises"

    # HOTEL INFO
    
    data['Name']= "Entertainment Cruises NY"
    data['S_Name']= 1 
    data['Address']= "Pier 62, Chelsea Piers Suite 200"
    data['S_Address']= 1
    data['City']= "New York"
    data['S_City']= 1
    data['State']= "NY"
    data['S_State']= 1
    data['Zip']= "10011"
    data['S_Zip']= 1
    data['Industry']= ""
    data['S_Industry']= 4
    data['Description'] = [{
            #This USES THE FACTCARD MACRO
            #Title of the card
            'fc_SubTitle':'Full Description',
            'fc_DescriptionsSize':'1',
            'fc_Descriptions': {
                            'd1': ['en',1 ,'Get up close to the Statue of Liberty and travel under the iconic Brooklyn Bridge. Come out for a cruise on beautiful New York Harbor from your choice of our dock at Chelsea Piers or Lincoln Harbor Marina in Weehawken, New Jersey.'], 
                            'd2': ['sp',4,'(Not spanish translation.)'],  
                            'd3': ['it',4,'(Not italian translation.)'],
                        }

            }]# CLOSE


    data['OneLine'] = [{
                #This USES THE FACTCARD MACRO
                #Title of the card
                'fc_SubTitle':'One Line Description',
                'fc_DescriptionsSize':'2',
                'fc_Descriptions': {
                            'd1': ['en',1 ,'Entertainment Cruises, dining cruises, yacht charters and sightseeing tours.'], 
                            'd2': ['sp',4,'(not spanish translation)'],  
                            'd3': ['it',4,'(not italian translation)'], 
                        }
                }]# CLOSE
    #CONTACT
    data['S_Website']= 1
    data['Website']= "http://www.bateauxnewyork.com/new-york-metro"
    data['Mail']= "explore@bikethebigapple.com "
    data['S_Mail']= 1
    data['Phone']= "866-817-3463"
    data['S_Phone']= 1
    data['Fax']= ""
    data['S_Fax']= 4
    data['Newsletter']= ""
    data['S_Newsletter']= 5
    data['Blog']= "ttp://www.entertainmentcruises.com/blog/"
    data['S_Blog']= 1

    #DETAILS
    data['Founded']= "x18"
    data['S_Founded']= 1
    data['Closed']= "x18"
    data['SClosed']= 1
    data['ResAge']= "x09"
    data['S_ResAge']= 1
    data['Founded']= "x10"
    data['S_Founded']= 1
    data['payments']="x12"
    data['S_payments']=1
    #SOCIALMEDIA  
        # twitter
    data['SM1']= "http://twitter.com/entertaincruise"
    data['S_SM1']= 1
        # facebook
    data['SM2']= "https://www.facebook.com/BateauxNewYork"
    data['S_SM2']= 1
        # instagram
    data['SM3']= "ecnewyork"
    data['S_SM3']= 4
        # youtube
    data['SM4']= "ecnewyork"
    data['S_SM4']= 4
        #Other Links
    data['LINK1']= ""
    data['S_LINK1']= 1
    data['LINK2']= ""
    data['S_LINK2']= 1
    data['LINK3']= ""
    data['S_LINK3']= 1
    data['LINK4']= ""
    data['S_LINK4']= 1
    #HISTORY
    data['Facts']= ""
    data['S_Facts']= 1
    data['Awards']= ""
    data['S_Awards']= 1
    data['FAQ']= ""
    data['FactualID']= ""
    data['history'] = [{
                    #This USES THE FACTCARD MACRO
                    #Title of the card
                    'fc_SubTitle':'History',
                    # Fields used:  History, History2, History3
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'Entertainment Cruises roots date back to 1978 when the Spirit of Norfolk was christened and began cruising the historic Elizabeth River. Today, we have 30 boats across nine locations and host more than 1.5 million guests each year. Our shipmates feel privileged to share in our guests special celebrations - and help make their experiences with us memorable.'], 
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'], 
                        },
                    # HISTORY PHOTOS
                    'fc_Owner':'teamamerica',
                    # PHOTOS
                    'fc_SmartPhotos': {
                            
                        }
                    
                    }]# CLOSE
    data['staff'] = [{
                    'fc_SubTitle':'Our Staff',
                    'fc_Descriptions': {
                        'd1': ['en',1,' No Description'],
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'],
                        
                        },
                    'fc_SmartPhotos': {
                            
                        }
                    }]# CLOSE

    data['curious'] = [{
                    'fc_SubTitle':'Facts',
                    'fc_Specs': {
                            'd1': ['Fact1','We have presence in 8 cities'], 
                            'd2': ['Fact2','Miles navigated each year'],  
                            'd3': ['Fact3','Our most popular cruise is Bateaux'], 
                        },
                    }]# CLOSE

    data['contact'] = [{
                    'fc_SubTitle':'Contact',
                    'fc_List': {
                            'd1': ['Website','http://www.entertainmentcruises.com/our-cities/new-york'], 
                            'd2': ['Mail','explore@bikethebigapple.com'],  
                            'd3': ['Phone','866-433-9283'], 
                        }

                    }]# CLOSE

    data['Services'] = [

                # START ITEM A
                {
                    'fc_Title':'Bateaux New York',
                    'S_fc_Title':1,
                    'fc_SubTitle':'Upscale. Exceptional.',
                    'S_fc_SubTitle':1,
                    'fc_Category':'Cruise Waterfront',
                    'S_fc_Category':1,
                    'fc_Specs': {
                            'd1': ['Category','Dinning Cruise'], 
                            'd2': ['Minimum Booking Age','18'],  
                            'd3': ['Attire','Casual'], 
                        },
                    'S_fc_Specs':1,
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'Get ready for the ultimate dining experience. Cruising year-round from Chelsea Piers, European-inspired Bateaux New York offers champagne brunch, lunch, dinner and full moon cruises, plus dozens of holiday cruises.'], 
                        'd2': ['sp',4,'Preparate para la mas emocionante experiencia mientras comes una cena de lujo. Operamos todo el ano desde el puerto de Chelsea. Inspirado en el estilo europeo, ofrecemos champagne, brunch, lunch, comidas y cruceros de luna llena, ademas de muchas experiencias en distintas fiestas y aniversarios.'],  
                        'd3': ['it',4,'(not italian translation)'],
                        },
                    'fc_Owner':'ecruises',
                    'fc_SmartPhotos': {
                            'p1': [1,'4965947608','ok'], 
                            'p2': [2,'4160860566','ok'],  
                            'p3': [3,'3424159261','ok'], 
                            'p4': [4,'6910202122','ok'],
                            
                        },
                    
                    'fc_Schedule': {
                            'd1': ['Monday','14:00','21:00',1], 
                            'd2': ['Tuesday','10:00','21:00',1],  
                            'd3': ['Wednesday','10:00','21:00',1], 
                            'd4': ['Thursday','10:00','21:00',1], 
                            'd5': ['Friday','10:00','21:00',1], 
                            'd6': ['Saturday','11:00','19:00',1], 
                            'd7': ['Sunday','11:00','19:00',1], 
                            },  
                    'fc_SmallNotes': {
                            'd1': ['Notes','Boarding is 30 minutes prior departure from Chelsea Pier, Pier 61 West 23rd Street and 12th Avenue. Dinner Sailing times: 7:00 to 10:00 pm. Brunch and Lunch Sailing Time: 12:00 to 2:00 pm. Schedule may change and boarding and departure time will be advised at time of confirmation of service.'], 
                            'd2': ['Dress Code','We request no jeans, shorts, tank tops, halter-tops, gym shoes or flip flops are worn on any cruise, Dinner: Jackets are recommended for men and cocktail attire for women.  Lunch: We recommend dressy casual attire, such as nice slacks and collared shirts. ']
                        },
                        'S_fc_SmallNotes':1
                },
                # CLOSE ITEM
                # START ITEM B
                {
                    'fc_Title':'Spirit Cruises',
                    'S_fc_Title':1,
                    'fc_SubTitle':'Fresh, Fun',
                    'S_fc_SubTitle':1,
                    'fc_Category':'Cruise',
                    'S_fc_Category':1,
                    'fc_Specs': {
                            'd1': ['Category','Dinning Cruise'], 
                            'd2': ['Minimum Booking Age','18'],  
                            'd3': ['Attire','Casual'], 
                        },
                    'S_fc_Specs':1,
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'Get ready for the time of your life aboard one of our two recently renovated ships departing from both New York and New Jersey. Sample a variety of dishes. Dance. And head topside to feel the wind in your hair. Join us aboard Spirit of New York and Spirit of New Jersey for a fun mix of dining, dancing, entertainment and skyline views. Cruising the Hudson River year-round, Spirit has a variety of lunch, dinner, moonlight and holiday cruises like Mother`s Day, plus dozens of themed cruises, to choose from.'], 
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'], 
                        },
                    'fc_Owner':'ecruises',
                    'fc_SmartPhotos': {
                            'p1': [1,'2002365081','ok'], 
                            'p2': [2,'1461327909','ok'],  
                            'p3': [3,'3424159261','ok'], 
                            'p4': [4,'6910202122','ok'],
                            },
                    'fc_Tags':[{
                                }, 
                            ],
                    'fc_Schedule': {
                            'd1': ['Monday','14:00','21:00',1], 
                            'd2': ['Tuesday','10:00','21:00',1],  
                            'd3': ['Wednesday','10:00','21:00',1], 
                            'd4': ['Thursday','10:00','21:00',1], 
                            'd5': ['Friday','10:00','21:00',1], 
                            'd6': ['Saturday','11:00','19:00',1], 
                            'd7': ['Sunday','11:00','19:00',1], 
                            },
                    'fc_SmallNotes': {
                            'd1': ['','']
                        },
                        'S_fc_SmallNotes':1

                },
                # CLOSE ITEM
                # START ITEM C
                {
                    'fc_Title':'Elite Private Yatch',
                    'S_fc_Title':1,
                    'fc_SubTitle':'Customizable. Private.',
                    'S_fc_SubTitle':1,
                    'fc_Category':'Cruise',
                    'S_fc_Category':1,
                    'fc_Specs': {
                            'd1': ['Category','Dinning Cruise'], 
                            'd2': ['Minimum Booking Age','18'],  
                            'd3': ['Attire','Formal'], 
                        },
                    'S_fc_Specs':1,
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'Host an exclusive event on New York Harbor on one of two private yachts. Atlantica or Manhattan Elite. Customize your charter with a variety of menu, decor, entertainment and route options. It`s your very own NYC private yacht. With sensational skyline views and completely customizable options, the Atlantica and Manhattan Elite offer two great ways to host an amazing and unique event aboard your own private yacht.'], 
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'], 
                        },
                    'fc_Owner':'ecruises',
                    'fc_SmartPhotos': {
                            'p1': [1,'4965947608','ok'], 
                            'p2': [2,'4160860566','ok'],  
                            'p3': [3,'3424159261','ok'], 
                            'p4': [4,'6910202122','ok'],
                            },
                    'fc_Tags':[{
                                }, 
                            ],
                    'fc_Schedule': {
                            'd1': ['Monday','14:00','21:00',1], 
                            'd2': ['Tuesday','10:00','21:00',1],  
                            'd3': ['Wednesday','10:00','21:00',1], 
                            'd4': ['Thursday','10:00','21:00',1], 
                            'd5': ['Friday','10:00','21:00',1], 
                            'd6': ['Saturday','11:00','19:00',1], 
                            'd7': ['Sunday','11:00','19:00',1], 
                            }, 
                    'fc_SmallNotes': {
                            'd1': ['','']
                        },
                        'S_fc_SmallNotes':1

                },
                # CLOSE ITEM
                

                
            


                    ] 

    return render_template("/sandbox/factcard.html", data=data) 


@app.route('/facts/bikethebigapple/<showme>')
#@login_required
def facts_004(showme):

    data = {}
    data['mask']= "mbf"
    data['mode']= showme
    data['slug']= "bikethebigapple"

    # HOTEL INFO
    
    data['Name']= "Bike the Big Apple"
    data['S_Name']= 1 
    data['Address']= ""
    data['S_Address']= 1
    data['City']= ""
    data['S_City']= 2
    data['State']= ""
    data['S_State']= 3
    data['Zip']= ""
    data['S_Zip']= 2
    data['Industry']= ""
    data['S_Industry']= 4
    data['Description'] = [{
            #This USES THE FACTCARD MACRO
            #Title of the card
            'fc_SubTitle':'Full Description',
            'fc_DescriptionsSize':'1',
            'fc_Descriptions': {
                            'd1': ['en',1 ,'For over fourteen years, we have been providing the absolute best and safest way of bringing visitors and residents alike far off the beaten path to see, feel, and experience the real New York. You will find that on our tours, you will surely see the sights the typical tourist seldom sees!. Whether you want to maximize the amount of New York that you experience, want to learn a whole lot about what is behind our city, or just want to have an utter blast, come tour with us.'], 
                            'd2': ['sp',4,'(Not spanish translation.)'],  
                            'd3': ['it',4,'(Not italian translation.)'],
                        }

            }]# CLOSE


    data['OneLine'] = [{
                #This USES THE FACTCARD MACRO
                #Title of the card
                'fc_SubTitle':'One Line Description',
                'fc_DescriptionsSize':'2',
                'fc_Descriptions': {
                            'd1': ['en',1 ,'Welcome to New York`s premier bicycle touring company'], 
                            'd2': ['sp',4,'(not spanish translation)'],  
                            'd3': ['it',4,'(not italian translation)'], 
                        }
                }]# CLOSE
    #CONTACT
    data['S_Website']= 1
    data['Website']= "www.bikethebigapple.com"
    data['Mail']= "explore@bikethebigapple.com "
    data['S_Mail']= 1
    data['Phone']= "1-347-878-9809"
    data['S_Phone']= 1
    data['Fax']= ""
    data['S_Fax']= 4
    data['Newsletter']= ""
    data['S_Newsletter']= 5
    data['Blog']= ""
    data['S_Blog']= 1

    #DETAILS
    data['Founded']= "x18"
    data['S_Founded']= 1
    data['Closed']= "x18"
    data['SClosed']= 1
    data['ResAge']= "x09"
    data['S_ResAge']= 1
    data['Founded']= "x10"
    data['S_Founded']= 1
    data['payments']="x12"
    data['S_payments']=1
    #SOCIALMEDIA  
        # twitter
    data['SM1']= "http://twitter.com/bikethebigapple"
    data['S_SM1']= 1
        # facebook
    data['SM2']= "http://www.facebook.com/pages/Bike-the-Big-Apple/373495324184"
    data['S_SM2']= 1
        # instagram
    data['SM3']= ""
    data['S_SM3']= 1
        # youtube
    data['SM4']= ""
    data['S_SM4']= 1
        #Other Links
    data['LINK1']= "x23"
    data['S_LINK1']= 1
    data['LINK2']= "x23"
    data['S_LINK2']= 1
    data['LINK3']= "x23"
    data['S_LINK3']= 1
    data['LINK4']= "x23"
    data['S_LINK4']= 1
    #HISTORY
    data['Facts']= "x14"
    data['S_Facts']= 1
    data['Awards']= "x14"
    data['S_Awards']= 1
    data['FAQ']= "x14"
    data['FactualID']= "x14"
    data['history'] = [{
                    #This USES THE FACTCARD MACRO
                    #Title of the card
                    'fc_SubTitle':'History',
                    # Fields used:  History, History2, History3
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'For well over a decade, we have been proud to be the largest, most successful company to offer fully-escorted bicycle tours throughout the five boroughs of the Big Apple. We take you beyond the usual tourist spots that bus and walking tours usually miss. And travelling by bike, you will come to appreciate, is the perfect way to truly experience the diverse neighborhoods of the city. On a bike tour, you will feel as though you are really part of the neighborhood. Walking tours & bus tours are certainly a nice way to see the city but bikes offer the best of both worlds (and more!). When compared to a day as pedestrian in New York, our leisurely paced rides are effortless and cover much more ground. And, you are able to interact with your surroundings much more than when on a bus. We feel certain you will leave with stories and photos that even the `natives` do not know about. '], 
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'], 
                        },
                    # HISTORY PHOTOS
                    'fc_Owner':'teamamerica',
                    # PHOTOS
                    'fc_SmartPhotos': {
                            
                        }
                    
                    }]# CLOSE
    data['staff'] = [{
                    'fc_SubTitle':'Our Staff',
                    'fc_Descriptions': {
                        'd1': ['en',1,'We are not a bike rental shop that also does bike tours or a walking/bus tour company that also does bike tours. Bike tours are all that we do. It is our focus, so we do it right. '],
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'],
                        
                        },
                    'fc_SmartPhotos': {
                            
                        }
                    }]# CLOSE

    data['curious'] = [{
                    'fc_SubTitle':'Facts',
                    'fc_Specs': {
                            'd1': ['Fact1','Each day, more than 250,000 cyclists ride in New York City, more than at any time in the last 25 years'], 
                            'd2': ['Fact2','A 2003 a report by Jacobsen showed that: The more bicyclists there are on the streets, the safer they are.'],  
                            'd3': ['Fact3','Bike riders are subject to the same laws as drivers in New York'], 
                            'd4': ['Fact4','Bike Friendly Business campaign exists to cultivate relationships with local businesses to encourage safe and lawful bicycling behavior'], 
                            'd5': ['Fact5','Eighty percent of the total cost of the 250 miles of bike lanes installed since 2006 was paid for by the federal government'], 
                            'd6': ['Fact6','Bike lanes can boost business. Streets that prioritize walking and biking, incorporated with amenities such as pedestrian plazas, have proven to boost local retail sales by 10-25 percent in cities around the world'], 
                            'd7': ['Fact7','Any person riding a bike can receive a ticket for not observing local transit laws.'], 
                            'd8': ['Fact8','there was a 13 percent increase in daily commuter bicycling between 2009 and 2010 alone']
                        },
                    }]# CLOSE

    data['contact'] = [{
                    'fc_SubTitle':'Contact',
                    'fc_List': {
                            'd1': ['Website','www.bikethebigapple.com'], 
                            'd2': ['Mail','explore@bikethebigapple.com'],  
                            'd3': ['Phone','1-347-878-9809'], 
                        }

                    }]# CLOSE

    data['Services'] = [

                # START ITEM A
                {
                    'fc_Title':'Tour A - The Ethnic Apple Tour.',
                    'S_fc_Title':1,
                    'fc_SubTitle':'Our ethnic mosaic tour',
                    'S_fc_SubTitle':1,
                    'fc_Category':'Bike Tour',
                    'S_fc_Category':1,
                    'fc_Specs': {
                            'd1': ['Category','Bike Tour'], 
                            'd2': ['Duration','7hrs'], 
                            'd3': ['MinAge','10'],  
                            'd4': ['Attire','Casual/ Sport'],
                            'd5': ['MinPax','4'], 
                            'd6': ['Season','All'], 
                        },
                    'S_fc_Specs':1,
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'Great urban vistas that are typically not seen. Ethnic neighborhoods that are part of the unique mosaic of the city. This great bike tour combines them both!. Our tour begins with a ride over the imposing Queensboro Bridge high over the East River. Don`t be confused by this bridge`s identity. Immortalized in popular music under its nickname, the bridge has recently been officially renamed after one of the city`s most charismatic, zaniest mayors ever. Once we`ve entered Queens, we`ll head to Gantry State Park. At this historic location we can see restored `gantries` and learn about their critical role in the city`s commerce in the first part of the 20th century. The view across the East River, directly opposite the United Nations and what was the world`s tallest apartment building, provides an unforgettable photo opportunity.'], 
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'],
                        },
                    'fc_Owner':'teamamerica',
                    'fc_SmartPhotos': {
                            'p1': [1,'4261055295','ok'], 
                            'p2': [2,'7452298333','ok'],  
                            'p3': [3,'7230214040','ok'], 
                            
                        },
                    'fc_Tags':[{'name': 'Includes', 
                                'list': ['bike','helmet','insurance'],
                                'status': 4
                                }, 
                            ],
                    'fc_Schedule': {
                            
                            'd1': ['Friday','10:100','17:00',1], 
                            'd2': ['On request','(min5 pax)','',4],
                            
                            },  
                    'fc_SmallNotes': {
                            'd1': ['Notes','This tour leaves every Friday, year-round, weather permitting, at 10:00 am from the Upper East Side of Manhattan (near the 68th street on the #6 subway) (precise address will be given after booking is made). It is approximately 15 miles and will last about 7 hours. (It is also available, by special request, any weekday)']
                        },
                        'S_fc_SmallNotes':1
                },
                # CLOSE ITEM
                # START ITEM B
                {
                    'fc_Title':'Tour B - The Delights of Brooklyn.',
                    'S_fc_Title':1,
                    'fc_SubTitle':'Brews, Views, Chocolate, and much more!',
                    'S_fc_SubTitle':1,
                    'fc_Category':'Bike Tour',
                    'S_fc_Category':1,
                    'fc_Specs': {
                            'd1': ['Category','Bike Tour'], 
                            'd2': ['Duration','7hrs'], 
                            'd3': ['MinAge','10'],  
                            'd4': ['Attire','Casual/ Sport'],
                            'd5': ['MinPax','4'], 
                            'd6': ['Season','All'], 
                        },
                    'S_fc_Specs':1,
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'This special tour starts with a ride through the historic Lower East Side. Once the most densely populated neighborhood in the world(!), it is now a very `in` section with a thriving nightlife, as well as an authentic Soviet era, larger than life, statue of Lenin. Leaving Manhattan, we dive into the delights offered by the borough of Brooklyn as we pedal over the new Williamsburg Bridge bike path. We enter the `hip,` artistic neighborhood of Williamsburg and head to one of the Big Apple`s truly underground micro-brewery. Here you can sample its artisinal beers and ale, or stout on tap.'], 
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'], 
                        },
                    'fc_Owner':'teamamerica',
                    'fc_SmartPhotos': {
                            'p1': [1,'7893794577','hi res'], 
                            'p2': [2,'3152079455','ok res'],  
                            'p4': [4,'5947166861','low res'], 
                        },
                    'fc_Tags':[{'name': 'Includes', 
                                'list': ['bike','helmet','insurance'],
                                'status': 4
                                }, 
                            ],
                    'fc_Schedule': {
                            
                            'd1': ['Saturday','10:15','17:00',1],
                            'd2': ['On request','(min5 pax)','',4],
                            
                            },  
                    'fc_SmallNotes': {
                            'd1': ['Notes','This tour leaves every Saturday, year-round, weather permitting, at 10:15 am, a few blocks from Union Square, of Manhattan (precise address will be given after booking is made). It is approximately 15 miles and will last about 7 hours. (It is also available, by special request, any weekday)']
                        },
                        'S_fc_SmallNotes':1

                },
                # CLOSE ITEM
                # START ITEM C
                {
                    'fc_Title':'Tour C - The Sensational Park and Soul Tour.',
                    'S_fc_Title':1,
                    'fc_SubTitle':'Bike the green Apple',
                    'S_fc_SubTitle':1,
                    'fc_Category':'Bike Tour',
                    'S_fc_Category':1,
                    'fc_Specs': {
                            'd1': ['Category','Bike Tour'], 
                            'd2': ['Duration','7hrs'], 
                            'd3': ['MinAge','10'],  
                            'd4': ['Attire','Casual/ Sport'],
                            'd5': ['MinPax','4'], 
                            'd6': ['Season','All'], 
                        },
                    'S_fc_Specs':1,
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'On this bike tour of Central Park and Harlem, we start on the East Side of Manhattan, the city`s wealthiest neighborhood with extravagant brownstones and mansions. Next door is Central Park, which never fails to amaze with its sheer natural beauty (all man-made). As we pedal through the park we`ll visit Strawberry Fields, the only `beach` on Manhattan Island, the North Woods loch, an authentic 3500 year old obelisk, an $18 million lawn, as well as one of the largest stands of still surviving magnificent elms in the western world. Highlights in Harlem include a live Sunday gospel service, as well as a dramatic poetry reading by the home of the `Black` Carl Sandberg. We`ll see Clinton`s new office and a former grand synagogue that is now a major Black church! We`ll even hear `Sachmo` playing a composition by `the Duke` beneath an unusual statue to this great composer. Enjoy a `Bike and Bite` soul food lunch in Harlem. '], 
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'], 
                        },
                    'fc_Owner':'teamamerica',
                    'fc_SmartPhotos': {
                            'p1': [1,'7078181063','hi res'], 
                            'p2': [2,'8885682710','ok res'],   
                        },
                    'fc_Tags':[{'name': 'Includes', 
                                'list': ['bike','helmet','insurance'],
                                'status': 4
                                }, 
                            ],
                    'fc_Schedule': {
                            
                            'd1': ['Saturday','10:15','17:00',1],
                            'd2': ['On request','(min5 pax)','',4],
                            
                            },  
                    'fc_SmallNotes': {
                            'd1': ['Notes','This tour leaves every Sunday, year-round, weather permitting, at 10:00 am from the Upper East Side of Manhattan (near the 68th street on the #6 subway) (precise address will be given after booking is made). It is approximately 12 miles and lasts about 5 hours. (It is also available, by special request, any weekday)']
                        },
                        'S_fc_SmallNotes':1

                },
                # CLOSE ITEM
                # START ITEM D
                {
                    'fc_Title':'Tour D - Secret Streets',
                    'S_fc_Title':1,
                    'fc_SubTitle':'From High Finance to Hidden Chinatown',
                    'S_fc_SubTitle':1,
                    'fc_Category':'Bike Tour',
                    'S_fc_Category':1,
                    'fc_Specs': {
                            'd1': ['Category','Bike Tour'], 
                            'd2': ['Duration','7hrs'], 
                            'd3': ['MinAge','10'],  
                            'd4': ['Attire','Casual/ Sport'],
                            'd5': ['MinPax','4'], 
                            'd6': ['Season','All'], 
                        },
                    'S_fc_Specs':1,
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'Get ready for a true New York bike tour that has you smack in the middle of New York City`s action. First, we head past Union Square, the place of every protest, from basic to bizarre. Next, we`re in Greenwich Village at the Stonewall Inn, symbol of the Gay Liberation movement. From `the Village,` we ride along the Hudson River Greenway to Wall Street, where we are caught up in the frantic pace of high finance. Bankers rub shoulders with bike messengers, and brokers down their lunch as fast as the fluctuation of the stock market. Then to Ground Zero, to experience that tragic day and the agonizing months that followed. In typical New York fashion, the city has bounced back. The new Number 7 World Trade Center, with its amazing streaming video, captures this sense of optimism.'], 
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'],
                        },
                    'fc_Owner':'teamamerica',
                    'fc_SmartPhotos': {
                            'p1': [1,'2602344552'], 
                            'p2': [2,'5054080943'],  
                        },
                    'fc_Tags':[{'name': 'Includes',
                                'list': ['bike','helmet','insurance'],
                                'status': 4
                                }, 
                            ],
                    'fc_Schedule': {
                            
                            'd1': ['Tuesday','10:15','17:00',1],
                            'd2': ['On request','(min5 pax)','',4], 
                            
                            },  
                    'fc_SmallNotes': {
                            'd1': ['Notes','This tour leaves every Tuesday, year-round, weather permitting, at 10:15 am, a few blocks from Union Square in Manhattan (precise address will be given after booking is made). It is approximately 14 miles and will last about 7 hours.']
                        },
                        'S_fc_SmallNotes':1

                },
                # CLOSE ITEM

                
            


                    ] 

    return render_template("/sandbox/factcard.html", data=data) 


@app.route('/facts/moma/<showme>')
#@login_required
def facts_005(showme):

    data = {}
    data['mask']= "mbf"
    data['mode']= showme
    data['slug']= "moma"

    # HOTEL INFO
    
    data['Name']= "Museum of Modern Art"
    data['S_Name']= 1 
    data['Address']= "11 West 53 Street"
    data['S_Address']= 1
    data['City']= "New York"
    data['S_City']= 1
    data['State']= "NY"
    data['S_State']= 1
    data['Zip']= "10019"
    data['S_Zip']= 1
    data['Industry']= ""
    data['S_Industry']= 4
    data['Description'] = [{
            #This USES THE FACTCARD MACRO
            #Title of the card
            'fc_SubTitle':'Full Description',
            'fc_DescriptionsSize':'1',
            'fc_Descriptions': {
                            'd1': ['en',1 ,'The Museum of Modern Art (MoMA) is a place that fuels creativity, ignites minds, and provides inspiration. Its exhibitions and collection of modern and contemporary art are dedicated to helping you understand and enjoy the art of our time.'], 
                            'd2': ['sp',4,'(Not spanish translation.)'],  
                            'd3': ['it',4,'(Not italian translation.)'],
                        }

            }]# CLOSE


    data['OneLine'] = [{
                #This USES THE FACTCARD MACRO
                #Title of the card
                'fc_SubTitle':'One Line Description',
                'fc_DescriptionsSize':'2',
                'fc_Descriptions': {
                            'd1': ['en',1 ,'Art exhibitions & Film'], 
                            'd2': ['sp',4,'(not spanish translation)'],  
                            'd3': ['it',4,'(not italian translation)'], 
                        }
                }]# CLOSE
    #CONTACT
    data['S_Website']= 1
    data['Website']= "http://www.moma.org/"
    data['Mail']= ""
    data['S_Mail']= 1
    data['Phone']= "(212) 708-9400"
    data['S_Phone']= 1
    data['Fax']= ""
    data['S_Fax']= 4
    data['Newsletter']= ""
    data['S_Newsletter']= 5
    data['Blog']= "http://www.moma.org/explore/inside_out"
    data['S_Blog']= 1

    #DETAILS
    data['Founded']= "1929"
    data['S_Founded']= 1
    data['Closed']= "x18"
    data['SClosed']= 1
    data['ResAge']= "x09"
    data['S_ResAge']= 1
    data['Founded']= "x10"
    data['S_Founded']= 1
    data['payments']="x12"
    data['S_payments']=1
    #SOCIALMEDIA  
        # twitter
    data['SM1']= "http://twitter.com/MuseumModernArt"
    data['S_SM1']= 1
        # facebook
    data['SM2']= "http://www.facebook.com/MuseumofModernArt"
    data['S_SM2']= 1
        # instagram
    data['SM3']= "https://instagram.com/themuseumofmodernart/"
    data['S_SM3']= 1
        # youtube
    data['SM4']= "http://www.youtube.com/user/MoMAvideos"
    data['S_SM4']= 1
        #Other Links
    data['LINK1']= ""
    data['S_LINK1']= 1
    data['LINK2']= ""
    data['S_LINK2']= 1
    data['LINK3']= ""
    data['S_LINK3']= 1
    data['LINK4']= ""
    data['S_LINK4']= 1
    #HISTORY
    data['Facts']= ""
    data['S_Facts']= 1
    data['Awards']= ""
    data['S_Awards']= 1
    data['FAQ']= ""
    data['FactualID']= ""
    data['history'] = [{
                    #This USES THE FACTCARD MACRO
                    #Title of the card
                    'fc_SubTitle':'History',
                    # Fields used:  History, History2, History3
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'In the late 1920s, three progressive and influential patrons of the arts, Miss Lillie P. Bliss, Mrs. Cornelius J. Sullivan, and Mrs. John D. Rockefeller, Jr., perceived a need to challenge the conservative policies of traditional museums and to establish an institution devoted exclusively to modern art. They, along with additional original trustees A. Conger Goodyear, Paul Sachs, Frank Crowninshield, and Josephine Boardman Crane, created The Museum of Modern Art in 1929. Its founding director, Alfred H. Barr, Jr., intended the Museum to be dedicated to helping people understand and enjoy the visual arts of our time, and that it might provide New York with "the greatest museum of modern art in the world.'], 
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'], 
                        },
                    # HISTORY PHOTOS
                    'fc_Owner':'teamamerica',
                    # PHOTOS
                    'fc_SmartPhotos': {
                            
                        }
                    
                    }]# CLOSE
    data['staff'] = [{
                    'fc_SubTitle':'Our Staff',
                    'fc_Descriptions': {
                        'd1': ['en',1,' No Description'],
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'],
                        
                        },
                    'fc_SmartPhotos': {
                            
                        }
                    }]# CLOSE

    data['curious'] = [{
                    'fc_SubTitle':'Facts',
                    'fc_Specs': {
                            'd1': ['Fact1','MoMA welcome millions of visitors every year'], 
                            'd2': ['Fact2','A still larger public is served by the Museum`s national and international programs of circulating exhibitions, loan programs, circulating film and video library, publications, Library and Archives holdings, websites, educational activities, special events, and retail sales.'],  
                            'd3': ['Fact3','Our most popular cruise is Bateaux'], 
                        },
                    }]# CLOSE

    data['contact'] = [{
                    'fc_SubTitle':'Contact',
                    'fc_List': {
                            'd1': ['Website','http://www.moma.org/'], 
                            'd2': ['Phone','(212) 708-9400'], 
                        }

                    }]# CLOSE

    data['Services'] = [

                # START ITEM A
                {
                    'fc_Title':'One-Way Ticket:',
                    'S_fc_Title':1,
                    'fc_SubTitle':'Jacob Lawrence`s Migration Series and Other Works',
                    'S_fc_SubTitle':1,
                    'fc_Category':'Art Exhbition',
                    'S_fc_Category':1,
                    'fc_Specs': {
                            'd1': ['Category','Painting, Photography, Documents'], 
                            'd2': ['Kids','yes'],  
                            'd3': ['Camera','No'], 
                        },
                    'S_fc_Specs':1,
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'In 1941, Jacob Lawrence, then just 23 years old, completed a series of 60 small tempera paintings with text captions about the Great Migration, the multi-decade mass movement of African Americans from the rural South to the urban North that started around 1915. Within months of its making, the series entered the collections of The Museum of Modern Art and the Phillips Memorial Gallery (today The Phillips Collection), with each institution acquiring half of the panels. Lawrence`s work is now an icon in both collections, a landmark in the history of modern art, and a key example of the way that history painting was radically reimagined in the modern era. One-Way Ticket: Jacob Lawrence`s Migration Series and Other Visions of the Great Movement North reunites all 60 panels for the first time at MoMA in 20 years.'], 
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'],
                        },
                    'fc_Owner':'teamamerica',
                    'fc_SmartPhotos': {
                            'p1': [1,'6896928037','ok'], 
                            'p2': [2,'3498992745','ok'],  
                            'p3': [3,'3836044439','ok'], 
                            'p4': [4,'6896928037','ok'],
                            
                        },
                    
                    'fc_Schedule': {
                            'd1': ['Exhbition','April 3','September 7, 2015',1],  
                            },  
                    'fc_SmallNotes': {
                            'd2': ['Additional Information','The exhibition is accompanied by a book, Jacob Lawrence: The Migration Series, copublished with The Phillips Collection, Washington D.C. With the opening of the exhibition, MoMA has created a rich multimedia website that explores each of Lawrence`s Migration panels, accompanied by a range of visual, auditory, literary, and documentary materials. The exhibition is also accompanied by a film series in MoMA`s theaters in June.']
                        },
                        'S_fc_SmallNotes':1
                },
                # CLOSE ITEM
                # START ITEM B
                {
                    'fc_Title':'Spirit Cruises',
                    'S_fc_Title':1,
                    'fc_SubTitle':'Fresh, Fun',
                    'S_fc_SubTitle':1,
                    'fc_Category':'Cruise',
                    'S_fc_Category':1,
                    'fc_Specs': {
                            'd1': ['Category','Dinning Cruise'], 
                            'd2': ['Minimum Booking Age','18'],  
                            'd3': ['Attire','Casual'], 
                        },
                    'S_fc_Specs':1,
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'Get ready for the time of your life aboard one of our two recently renovated ships departing from both New York and New Jersey. Sample a variety of dishes. Dance. And head topside to feel the wind in your hair. Join us aboard Spirit of New York and Spirit of New Jersey for a fun mix of dining, dancing, entertainment and skyline views. Cruising the Hudson River year-round, Spirit has a variety of lunch, dinner, moonlight and holiday cruises like Mother`s Day, plus dozens of themed cruises, to choose from.'], 
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'], 
                        },
                    'fc_Owner':'teamamerica',
                    'fc_SmartPhotos': {
                            'p1': [1,'6896928037','ok'], 
                            'p2': [2,'3498992745','ok'],  
                            'p3': [3,'3836044439','ok'], 
                            'p4': [4,'6896928037','ok'], 
                        },
                    'fc_Tags':[{
                                }, 
                            ],
                    'fc_Schedule': {
                            'd1': ['Monday','14:00','21:00',1], 
                            'd2': ['Tuesday','10:00','21:00',1],  
                            'd3': ['Wednesday','10:00','21:00',1], 
                            'd4': ['Thursday','10:00','21:00',1], 
                            'd5': ['Friday','10:00','21:00',1], 
                            'd6': ['Saturday','11:00','19:00',1], 
                            'd7': ['Sunday','11:00','19:00',1], 
                            },
                    'fc_SmallNotes': {
                            'd1': ['','']
                        },
                        'S_fc_SmallNotes':1

                },
                # CLOSE ITEM
                # START ITEM C
                {
                    'fc_Title':'Elite Private Yatch',
                    'S_fc_Title':1,
                    'fc_SubTitle':'Customizable. Private.',
                    'S_fc_SubTitle':1,
                    'fc_Category':'Cruise',
                    'S_fc_Category':1,
                    'fc_Specs': {
                            'd1': ['Category','Dinning Cruise'], 
                            'd2': ['Minimum Booking Age','18'],  
                            'd3': ['Attire','Formal'], 
                        },
                    'S_fc_Specs':1,
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'Host an exclusive event on New York Harbor on one of two private yachts. Atlantica or Manhattan Elite. Customize your charter with a variety of menu, decor, entertainment and route options. It`s your very own NYC private yacht. With sensational skyline views and completely customizable options, the Atlantica and Manhattan Elite offer two great ways to host an amazing and unique event aboard your own private yacht.'], 
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'], 
                        },
                    'fc_Owner':'teamamerica',
                    'fc_SmartPhotos': {
                            'p1': [1,'6896928037','ok'], 
                            'p2': [2,'3498992745','ok'],  
                            'p3': [3,'3836044439','ok'], 
                            'p4': [4,'6896928037','ok'], 
                        },
                    'fc_Tags':[{
                                }, 
                            ],
                    'fc_Schedule': {
                            'd1': ['Monday','14:00','21:00',1], 
                            'd2': ['Tuesday','10:00','21:00',1],  
                            'd3': ['Wednesday','10:00','21:00',1], 
                            'd4': ['Thursday','10:00','21:00',1], 
                            'd5': ['Friday','10:00','21:00',1], 
                            'd6': ['Saturday','11:00','19:00',1], 
                            'd7': ['Sunday','11:00','19:00',1], 
                            }, 
                    'fc_SmallNotes': {
                            'd1': ['','']
                        },
                        'S_fc_SmallNotes':1

                },
                # CLOSE ITEM
                       


                    ] 

    return render_template("/sandbox/factcard.html", data=data) 


@app.route('/facts/madmuseum/<showme>')
#@login_required
def facts_006(showme):

    data = {}
    data['mask']= "mbf"
    data['mode']= showme
    data['slug']= "madmuseum"

    # HOTEL INFO
    
    data['Name']= "Museum of arts and design"
    data['S_Name']= 1 
    data['Address']= "2 columbus Circle"
    data['S_Address']= 1
    data['City']= "New York"
    data['S_City']= 1
    data['State']= "NY"
    data['S_State']= 1
    data['Zip']= "10019"
    data['S_Zip']= 1
    data['Industry']= ""
    data['S_Industry']= 4
    data['Description'] = [{
            #This USES THE FACTCARD MACRO
            #Title of the card
            'fc_SubTitle':'Full Description',
            'fc_DescriptionsSize':'1',
            'fc_Descriptions': {
                            'd1': ['en',1 ,'The mission of the Museum of Arts and Design (MAD) is to collect, display, and interpret objects that document contemporary and historic innovation in craft, art, and design. In its exhibitions and educational programs, the Museum celebrates the creative process through which materials are crafted into works that enhance contemporary life.'], 
                            'd2': ['sp',4,'(Not spanish translation.)'],  
                            'd3': ['it',4,'(Not italian translation.)'],
                        }

            }]# CLOSE


    data['OneLine'] = [{
                #This USES THE FACTCARD MACRO
                #Title of the card
                'fc_SubTitle':'One Line Description',
                'fc_DescriptionsSize':'2',
                'fc_Descriptions': {
                            'd1': ['en',1 ,'Design, Art exhibitions & Film'], 
                            'd2': ['sp',4,'(not spanish translation)'],  
                            'd3': ['it',4,'(not italian translation)'], 
                        }
                }]# CLOSE
    #CONTACT
    data['S_Website']= 1
    data['Website']= "http://www.madmuseum.org/"
    data['Mail']= "info@madmuseum.org "
    data['S_Mail']= 1
    data['Phone']= "212-299-7777"
    data['S_Phone']= 1
    data['Fax']= ""
    data['S_Fax']= 4
    data['Newsletter']= ""
    data['S_Newsletter']= 5
    data['Blog']= ""
    data['S_Blog']= 1

    #DETAILS
    data['Founded']= "1956"
    data['S_Founded']= 1
    data['Closed']= "x18"
    data['SClosed']= 1
    data['ResAge']= "x09"
    data['S_ResAge']= 1
    data['Founded']= "x10"
    data['S_Founded']= 1
    data['payments']="x12"
    data['S_payments']=1
    #SOCIALMEDIA  
        # twitter
    data['SM1']= "http://www.twitter.com/madmuseum"
    data['S_SM1']= 1
        # facebook
    data['SM2']= "http://www.facebook.com/madmuseum"
    data['S_SM2']= 1
        # instagram
    data['SM3']= "http://instagram.com/madmuseum"
    data['S_SM3']= 1
        # youtube
    data['SM4']= ""
    data['S_SM4']= 1
        #Other Links
    data['LINK1']= ""
    data['S_LINK1']= 1
    data['LINK2']= ""
    data['S_LINK2']= 1
    data['LINK3']= ""
    data['S_LINK3']= 1
    data['LINK4']= ""
    data['S_LINK4']= 1
    #HISTORY
    data['Facts']= ""
    data['S_Facts']= 1
    data['Awards']= ""
    data['S_Awards']= 1
    data['FAQ']= ""
    data['FactualID']= ""
    data['history'] = [{
                    #This USES THE FACTCARD MACRO
                    #Title of the card
                    'fc_SubTitle':'History',
                    # Fields used:  History, History2, History3
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'The Museum first opened its doors in 1956 as the Museum of Contemporary Crafts, with an original mission of recognizing the craftsmanship of contemporary American artists. Nurtured by the vision of philanthropist and craft patron Aileen Osborn Webb, the Museum mounted exhibitions that focused on the materials and techniques associated with craft disciplines.'], 
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'], 
                        },
                    # HISTORY PHOTOS
                    'fc_Owner':'teamamerica',
                    # PHOTOS
                    'fc_SmartPhotos': {
                            
                        }
                    
                    }]# CLOSE
    data['staff'] = [{
                    'fc_SubTitle':'Our Staff',
                    'fc_Descriptions': {
                        'd1': ['en',1,' No Description'],
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'],
                        
                        },
                    'fc_SmartPhotos': {
                            
                        }
                    }]# CLOSE

    data['curious'] = [{
                    'fc_SubTitle':'Facts',
                    'fc_Specs': {
                            'd1': ['Fact1','Museum of arts and design was founded by philanthropist and visionary Aileen Osborn Webb'], 
                            'd2': ['Fact2',''],  
                            'd3': ['Fact3',''], 
                        },
                    }]# CLOSE

    data['contact'] = [{
                    'fc_SubTitle':'Contact',
                    'fc_List': {
                            'd1': ['Website','http://www.madmuseum.org'], 
                            'd2': ['Email','info@madmuseum.org'], 
                            'd3': ['Phone','212-299-7777'], 
                        }

                    }]# CLOSE
    data['photos'] = [{
                    
                    'fc_Owner':'teamamerica',
                    'fc_SmartPhotos': {
                            'p1': [1,'6896928037','ok'], 
                            'p2': [2,'3498992745','ok'],  
                            'p3': [3,'3836044439','ok'], 
                            'p4': [4,'6896928037','ok'], 
                            'p5': [4,'6896928037','ok'], 
                            'p6': [4,'6896928037','ok'], 
                        }

                    }]# CLOSE

    data['ServiceName'] ='Current exhibitions'
    data['Services'] = [

                # START ITEM A
                {
                    'fc_Title':'Ralph Pucci:',
                    'S_fc_Title':1,
                    'fc_SubTitle':'The Art of the Mannequin',
                    'S_fc_SubTitle':1,
                    'fc_Category':'Art Exhbition',
                    'S_fc_Category':1,
                    'fc_Specs': {
                            'd1': ['Category','Design, Fashion'], 
                            'd2': ['Kids','yes'],  
                            'd3': ['Camera','ok'], 
                        },
                    'S_fc_Specs':1,
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'Ralph Pucci: The Art of the Mannequin will be the first museum exhibition to explore the work of renowned New York-based designer Ralph Pucci, who is widely regarded for his innovative approach to the familiar form of the mannequin. Having collaborated with luminaries such as Diane von Furstenberg, Patrick Naggar, Andree Putman, Kenny Scharf, Anna Sui, Isabel and Ruben Toledo and Christy Turlington, Pucci`s mannequins not only expand the parameters of this ubiquitous sculptural form, but reflect major cultural trends of the past three decades.'], 
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'],
                        },
                    'fc_Owner':'teamamerica',
                    'fc_SmartPhotos': {
                            'p1': [1,'6896928037','ok'], 
                            'p2': [2,'3498992745','ok'],  
                            'p3': [3,'3836044439','ok'], 
                            'p4': [4,'6896928037','ok'],
                            
                        },
                    
                    'fc_Schedule': {
                            'd1': ['','APR 3','SEP 7, 2015',1],  
                            },  
                    'fc_SmallNotes': {
                            'd2': ['Organized by','MAD`s Chief Curator Lowery Stokes Sims and Barbara Paris Gifford, Curatorial Assistant and project manager, the exhibition will be accompanied by a publication that includes a foreword by Margaret Russell, editor in chief of Architectural Digest, an essay by art historian Emily M. Orr on the history of mannequins and an interview with Pucci by Jake Yuzna, Director of Public Programs at MAD.']
                        },
                        'S_fc_SmallNotes':1
                },
                # CLOSE ITEM
                # START ITEM 
                {
                    'fc_Title':'Richard Estes:',
                    'S_fc_Title':1,
                    'fc_SubTitle':'Painting New York City',
                    'S_fc_SubTitle':1,
                    'fc_Category':'Art Exhbition',
                    'S_fc_Category':1,
                    'fc_Specs': {
                            'd1': ['Category','Painting'], 
                            'd2': ['Kids','ok'],  
                            'd3': ['Camera','ok'], 
                        },
                    'S_fc_Specs':1,
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'Spanning from the mid-1960s to the present, Richard Estes: Painting New York City presents works by this quintessential New York artist and enduring leader of the Photorealist movement. Providing an unprecedented insight into the artist`s creative process, the exhibition reveals a full range of Estes paintings and works on paper, including his photographs, silkscreens and woodcuts and their various proofs, states, and art-making tools.'], 
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'],
                        },
                    'fc_Owner':'teamamerica',
                    'fc_SmartPhotos': {
                            'p1': [1,'6896928037','ok'], 
                            'p2': [2,'3498992745','ok'],  
                            'p3': [3,'3836044439','ok'], 
                            'p4': [4,'6896928037','ok'],
                            
                        },
                    
                    'fc_Schedule': {
                            'd1': ['','MAR 10','SEP 20, 2015',1],  
                            },  
                    'fc_SmallNotes': {
                            'd2': ['Organized by','MAD`s Marcia Docter Curator Ronald T. Labaco and Samantha De Tillio, Curatorial Assistant and Project Manager.  The exhibition will be accompanied by a fully-illustrated, full color catalogue.']
                        },
                        'S_fc_SmallNotes':1
                },
                # CLOSE ITEM
                # START ITEM 
                {
                    'fc_Title':'Pathmakers:',
                    'S_fc_Title':1,
                    'fc_SubTitle':'Women in Art, Craft and Design, Midcentury and Today',
                    'S_fc_SubTitle':1,
                    'fc_Category':'Art Exhbition',
                    'S_fc_Category':1,
                    'fc_Specs': {
                            'd1': ['Category','Crafts, Design'], 
                            'd2': ['Kids','ok'],  
                            'd3': ['Camera','ok'], 
                        },
                    'S_fc_Specs':1,
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'In the 1950s and 60s, an era when painting, sculpture, and architecture were dominated by men, women had considerable impact in alternative materials such as textiles, ceramics, and metals. Largely unexamined in major art historical surveys, either due to their gender or choice of materials, these pioneering women achieved success and international recognition, establishing a model of professional identity for future generations of women.'], 
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'],
                        },
                    'fc_Owner':'gcid',
                    'fc_SmartPhotos': {
                            'p1': [1,'3002987120','ok'], 
                            'p2': [2,'1136695178','ok'],  
                            'p3': [3,'1750768890','ok'], 
                            'p4': [4,'6889765353','ok'],
                            'p5': [4,'3698624088','ok'],
                            'p6': [4,'4452106848','ok'],
                            'p7': [4,'7592696236','ok'],
                            'p8': [4,'7592696236','ok'],
                            'p9': [4,'2104491229','ok'],
                            
                        },
                    
                    'fc_Schedule': {
                            'd1': ['','MAR 10','SEP 20, 2015',1],  
                            },  
                    'fc_SmallNotes': {
                            'd2': ['Organized by','guest curator Patterson Sims, along with Sophia Merkin, Curatorial Assistant and Project Manager.']
                        },
                        'S_fc_SmallNotes':1
                },
                # CLOSE ITEM
                # START ITEM 
                {
                    'fc_Title':'Wendell Castle',
                    'S_fc_Title':1,
                    'fc_SubTitle':'Remastered',
                    'S_fc_SubTitle':1,
                    'fc_Category':'Art Exhbition',
                    'S_fc_Category':1,
                    'fc_Specs': {
                            'd1': ['Category','Crafts, Design'], 
                            'd2': ['Kids','ok'],  
                            'd3': ['Camera','ok'], 
                        },
                    'S_fc_Specs':1,
                    'fc_Descriptions': {
                        'd1': ['en',1 ,'Wendell Castle Remastered will be the first museum exhibition to examine the digitally crafted works of Wendell Castle, acclaimed figure of the American art furniture movement. A master furniture maker, designer, sculptor, and educator, Castle is now in the sixth decade of a prolific career that began in 1958 one that parallels the emergence and growth of the American studio craft movement. In this solo exhibition, Castle casts a critical eye toward the first decade of his own artistic production by creating a new body of work that revisits his groundbreaking achievements of the 1960s through a contemporary lens. This self reflective meditation examines a crucial period during which Castle`s sculptural practices came to define his pivotal role as a leader in the field, and set the foundation for his longevity.'], 
                        'd2': ['sp',4,'(not spanish translation)'],  
                        'd3': ['it',4,'(not italian translation)'],
                        },
                    'fc_Owner':'teamamerica',
                    'fc_SmartPhotos': {
                            'p1': [1,'6896928037','ok'], 
                            'p2': [2,'3498992745','ok'],  
                            'p3': [3,'3836044439','ok'], 
                            'p4': [4,'6896928037','ok'],
                            
                        },
                    
                    'fc_Schedule': {
                            'd1': ['','OCT 20','FEB 28, 2016',1],  
                            },  
                    'fc_SmallNotes': {
                            'd2': ['Organized by','guest curator Patterson Sims, along with Sophia Merkin, Curatorial Assistant and Project Manager.']
                        },
                        'S_fc_SmallNotes':1
                },
                # CLOSE ITEM

                       


                    ] 

    return render_template("/sandbox/factcard.html", data=data) 




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


@app.route('/ecosystemb')
def ecosystemb():
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
