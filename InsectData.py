class InsectData:

    def spid(self):

        result = {}

        result['name'] =  'TOCATL v.0.2.3'
        result['title'] = 'Schema Modeler'
        result['subtitle'] = 'Model and edit your schemas'
        result['icon'] = 'r-spid.png'
        result['desc'] = "A schema defines the shape and characteristics the data will have during the Capture process. Designing a good schema from the beginning it's very important because it will make the info more usable. "
        result['slug'] = 'schema_modeler'
        result['label'] = 'mod'
        result['preview'] = 'f/spid1.png'
        result['step1'] = "Joining existing schemas created by expert Data modelers is the first best approach to start adding Data to your Rings."
        result['diag1'] = 'f/spid1.png'
        result['step2'] = "In case you can't find an appropriate schema that suits your needs you can either fork an existent one or create a new one from scratch."
        result['diag2'] = 'f/spid2.png'
        result['step3'] = "Schemas are build on top of Semantic vocabularies, making it love at first sight for RDF supporters."
        result['diag3'] = 'f/spid3.png'
        result['details'] = "1. RDF  (Resource Description Framework) facilitate data merging even if the sources differ. It also support the evolution of schemas over time without requiring any schema or data to be changed. 2. Data Modeler It's a tool intended to be used by more experienced users. the general recommendation is to start using existent schemas or fork existent ones. "

        return result


    def cica(self):
        
        result = {}

        result['name'] =  'CHIQUILICHTLI v.0.1.1'
        result['title'] = 'Semantic labeler'
        result['subtitle'] = 'Annotate your data semantically'
        result['icon'] = 'r-cica.png'
        result['desc'] = 'An annotation is metadata (e.g. a comment, explanation, markup) attached to text, image, or other data. This tool makes annotating Data extremely easy.'
        result['slug'] = 'semantic_labeler'
        result['label'] = 'mod'
        result['preview'] = 'phiw/ph02.png'
        result['step1'] = "This tool helps the data Modeler determine whether there is a vocabulary for what it's been modeled."
        result['diag1'] = 'phiw/ph03.png'
        result['step2'] = 'It leaves under the hood all the complexity of RFD, Triples, Linked Data, schemas,etc.'
        result['diag2'] = 'phiw/ph06.png'
        result['step3'] = 'It also helps to determine what is the proper datatype to use and even the widget that is going to be displayed in the GUI.'
        result['diag3'] = 'phiw/ph07.png'
        result['details'] = ""

        return result


    def dfly(self):

        result = {}

        result['name'] =  'ETZATL v.0.1.2'
        result['title'] = 'Manual Capture'
        result['subtitle'] = 'Capture all kind of Data manually'
        result['icon'] = 'r-dfly.png'
        result['desc'] = 'This tool enables anyone to create intuitive Forms and Wizards to collect data from collaborators. It also serves as the administration system to approve and discard data.'
        result['slug'] = 'manual_capture'
        result['label'] = 'cap'
        result['preview'] = 'phiw/ph02.png'
        result['step1'] = "Capture any kind of Data such as Strings, long texts,  Numeric Values, Boleans, Geolocations, Dates or any custom format."
        result['diag1'] = 'phiw/ph03.png'
        result['step2'] = "Capture Content such as photographs, sound, video, files and anything that can be uploaded via a desktop or mobile device."
        result['diag2'] = 'phiw/ph06.png'
        result['step3'] = "Register qualitative Data in familiar instruments such as questionnaires and surveys."
        result['diag3'] = 'phiw/ph07.png'
        result['details'] = ""

        return result


    def mosq(self):

        result = {}

        result['name'] =  'APIPILO v.0.1.2'
        result['title'] = 'Automatic Capture'
        result['subtitle'] = 'Capture your Data via sensors and devices.'
        result['icon'] = 'r-mosq.png'
        result['desc'] = "This tool allows any sensor to capture and store information in a Ring, Ideal for weather stations, traffic counters and any science based project that need to capture data automatically."
        result['slug'] = 'automatic_capture'
        result['label'] = 'cap'
        result['preview'] = 'phiw/ph02.png'
        result['step1'] = 'Register Quantitative Data without human manipulation or interference. '
        result['diag1'] = 'phiw/ph03.png'
        result['step2'] = 'IoT Ready: This tool help Data Device makers and/ or users to use Rings as a neutral way to share Raw Data across devices and systems.'
        result['diag2'] = 'phiw/ph06.png'
        result['step3'] = 'Compatible with any device or system sharing system via an API'
        result['diag3'] = 'phiw/ph07.png'
        result['details'] = ""

        return result  

        
    def worm(self):

        result = {}

        result['name'] =  'TEMOLIN 0.1.2'
        result['title'] = 'Legacy Data'
        result['subtitle'] = 'Bring your legacy Data back to life'
        result['icon'] = 'r-worm.png'
        result['desc'] = "Legacy Data is an Asset in which an organization may have invested significant resources, but has been created or stored by the use of software and/or hardware that has become obsolete or replaced "
        result['slug'] = 'legacy_data'
        result['label'] = 'cap'
        result['preview'] = 'phiw/ph02.png'
        result['step1'] = "Cleanup and uniform Legacy Data under a modern Data Schema."
        result['diag1'] = 'phiw/ph03.png'
        result['step2'] = "Keep track on how the legacy data was converted in order to convert it back and forth easily."
        result['diag2'] = 'phiw/ph06.png'
        result['step3'] = "In case a total data export is not the best option,  Rings can be used exclusively as a dynamic mask to convert Data to a new format"
        result['diag3'] = 'phiw/ph07.png'
        result['details'] = ""

        return result 

    def ants(self):

        result = {}

        result['name'] =  'AZCATL 0.1.2'
        result['title'] = 'Data Scrapper'
        result['subtitle'] = 'Use Data from other sources'
        result['icon'] = 'r-ants.png'
        result['desc'] = "Ants it's a tool that scrape existing data from not structurized sources such as HTML,  text files and several loose formats."
        result['slug'] = 'data_scrapper'
        result['label'] = 'cap'
        result['preview'] = ''
        result['step1'] = "Machine Learning techniques will improve your search algorithm over the time making your scrapping more effective."
        result['diag1'] = 'phiw/ph03.png'
        result['step2'] = "Selective scrapping will allow you to get only the information that you need without overwhelming the source."
        result['diag2'] = 'phiw/ph06.png'
        result['step3'] = "Make sense of scrapped data with the highly customizable pattern editor"
        result['diag3'] = 'phiw/ph07.png'
        result['details'] = ""

        return result      


    def bees(self):

        result = {}

        result['name'] =  'TLALPIPIOLLI v.1.2.0'
        result['title'] = 'Data Share'
        result['subtitle'] = "Serve your Data in multiple API flavors"
        result['icon'] = 'r-bees.png'
        result['desc'] = "This tool prepares your Data to be shared across multiple systems and platforms via an API "
        result['slug'] = 'data_share'
        result['label'] = 'sha'
        result['preview'] = 'phiw/ph02.png'
        result['step1'] = 'Control Panel for all APIs that expose/retrieve data from/for the rings'
        result['diag1'] = 'phiw/ph03.png'
        result['step2'] = "Publish your data from a menu of different API flavors (JSON-REST, XML-REST, SOAP, SPARQL, CSV, etc)"
        result['diag2'] = 'phiw/ph06.png'
        result['step3'] = "Understand your Data usage with an intuitive Panel Control"
        result['diag3'] = 'phiw/ph03.png'
        result['details'] = ""

        return result


    def lbug(self):

        result = {}

        result['name'] =  'MICAZOYOLIN 0.1.2'
        result['title'] = 'Data Website'
        result['subtitle'] = "Share your data in a rich web application"
        result['icon'] = 'r-lbug.png'
        result['desc'] = "This tool Autogenerate a friendly  HTML website with search and pagination so you can browse your data as a simple webpage in any desktop or mobile device."
        result['slug'] = 'data_website'
        result['label'] = 'sha'
        result['preview'] = 'phiw/ph06.png'
        result['step1'] = "Define how you want to see your Data and who you want to see it with privacy controls."
        result['diag1'] = 'phiw/ph01.png'
        result['step2'] = "Create a Single page Data Ticker to display all your data ala Wall Street. In Real Time as it's collected."
        result['diag2'] = 'phiw/ph11.png'
        result['step3'] = "MyRing love Data Visualizators. My Ring encourage any developer and designer to use Shared  public Data to create amazing infographic, charts and visualizations."
        result['diag3'] = 'phiw/ph06.png'
        result['details'] = ""

        return result


    def bfly(self):

        result = {}

        result['name'] =  'PAPALOTL v.0.1.2'
        result['title'] = 'Data Combinator'
        result['subtitle'] = 'Build your result across multiple Data sources'
        result['icon'] = 'r-bfly.png'
        result['desc'] = "This tool is the culmination of all the model and capture process. Combine, filter and merge your Rings with others to create the most incredible results. "
        result['slug'] = 'data_combinator'
        result['label'] = 'sha'
        result['preview'] = 'phiw/ph02.png'
        result['step1'] = "With Rings you have access to any public Data generated in any ring around the world, create rich results by combining Data of different Nature."
        result['diag1'] = 'phiw/ph03.png'
        result['step2'] = " Papalotl optimize respond times by caching results and by the use of an algorithm that separates volatile Data from static Data  that don't change often."
        result['diag2'] = 'phiw/ph06.png'
        result['step3'] = " Papalotl assumes that each ring contains different kind of data. It also discard a onesize-fit all approach and favors the use of smart filters that allows complex querying to multiple Data sources. "
        result['diag3'] = 'phiw/ph07.png'
        result['details'] = ""

        return result    
