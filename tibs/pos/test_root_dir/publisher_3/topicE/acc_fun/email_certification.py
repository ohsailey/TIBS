#-*- coding: utf-8 -*-
from flask import Flask, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from wtforms import form, fields, validators
from flask.ext import admin, login
from flask_admin.contrib import sqla
from flask_admin import helpers, expose
from flask import jsonify
from configobj import ConfigObj
from threading import Thread

# Create Flask application
app = Flask(__name__)

@app.route('/pushData/', methods=['POST', 'GET'])
def receiveData():
    if request.method == 'POST':
        pushDB(request.data)

@app.route('/checkCountry/', methods=['POST', 'GET'])
def readFolder():
    countryInfo = search_dir_file(1, 'C:/Users/Bai/workspace_python/Is_Setup/Config file')
    data = {
        'status' : 'OK',
        'data' : countryInfo
    }
    return jsonify(data)

@app.route('/Fetch/', methods=['POST', 'GET'])
def receiveReq():
    response = answer(request.data)
    return jsonify(response)

@app.route('/getCode/', methods=['POST', 'GET'])
def fetchCode():
    user = User.query.filter_by(id=login.current_user.get_id()).first()
    regionInfo = parseXmlFile('district')
    data = {
        'status' : 'OK',
        'regionInfo' : regionInfo
    }
    return jsonify(data)

@app.route('/readNationConfig/', methods=['POST', 'GET'])
def readConfigs():
    user = User.query.filter_by(id=login.current_user.get_id()).first()
    ConfigInfo = fetchConfigInfo(user.country,user.city)
    data = {
        'status' : 'OK',
        'configInfo' : ConfigInfo,
        'country' : user.country,
        'city' : user.city
    }
    return jsonify(data)

@app.route('/setup/', methods=['POST', 'GET'])
def setup():
    user = User.query.filter_by(id=login.current_user.get_id()).first()
    configInfo = fetchConfigInfo(user.country,user.city)
    #languageInfo = parseXmlFile('UIlanguage')
    wardInfo = parseXmlFile('district')
    data = {
        'status' : 'OK',
        'configInfo' : configInfo,
        'country' : user.country,
        'city' : user.city,
        'districtInfo' : wardInfo,
        #'uilanguage' : languageInfo
    }
    return jsonify(data)

@app.route('/fetchConfig/', methods=['POST', 'GET'])
def fetchConfigs():
    user = User.query.filter_by(id=login.current_user.get_id()).first()
    ConfigInfo = fetchConfigInfo(user.country,user.city)
    data = {
        'status' : 'OK',
        'data' : ConfigInfo,
        'country' : user.country,
        'city' : user.city,
    }
    return jsonify(data)

@app.route('/getShelter/', methods=['POST', 'GET'])
def retrieveShelterDb():
    public_data = []
    for s in db.session.query(Shelter):
        mapdata={
                'Id' : s.Id,
                'Name' : s.Name,
                'Type' : s.Type,
                'Category' : s.Category,
                'District' : s.District,
                'Address' : s.Address,
                'Telphone' : s.Telphone,
                'Latitude' : s.Latitude,
                'Longitude' : s.Longitude,
                'Description' : s.Description
        }
        public_data.append(mapdata)

    data = {
            'status' : 'OK',
            'data' : public_data
        }

    return jsonify(data)

@app.route('/getPOS/', methods=['POST', 'GET'])
def retrievePOSDb():
    public_data = []
    for s in db.session.query(POS):
        mapdata={
                'id' : s.POS_id,
                'district' : s.POS_district,
                'method' : s.Partition_method,
                'bound_Latlng1' : s.Rectangle_coordinate1,
                'bound_Latlng2' : s.Rectangle_coordinate2,
                'latitude' : s.POS_latitude,
                'longitude' : s.POS_longitude,
                'isContact' : s.Is_Available
        }
        public_data.append(mapdata)

    data = {
            'status' : 'OK',
            'data' : public_data
        }

    return jsonify(data)

@app.route('/UpdatePOS/', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        updatePOSDb(request.data)

@app.route('/Download/', methods=['POST', 'GET'])
def makefile():
    if request.method == 'POST':
        string = (request.data).split('$')
        createFolder(string[0])
        downloadTxt(string[0],string[1])
        #downloadImg(string[1],string[2])
@app.route('/Publish/', methods=['POST', 'GET'])
def Publish():
    if request.method == 'POST':
        postToHub(request.data)

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('hello', name = 'fuzai'))


import requests
import urllib
import urllib2
import os, sys
import json
import xml.etree.ElementTree as ET
import random


def answer(request):
    user = User.query.filter_by(id=login.current_user.get_id()).first()
    if request == 'cityInfo':
        ConfigInfo = fetchConfigInfo(user.country,user.city)
        data = {
            'status' : 'OK',
            'configInfo' : ConfigInfo,
            'country' : user.country,
            'city' : user.city
        }
    elif request == 'geoInfo':
        regionInfo = parseXmlFile('district')
        data = {
            'status' : 'OK',
            'regionInfo' : regionInfo
        }
    elif request == 'exist_Country$City':
        nationInfo = search_dir_file(1, 'C:/Users/Bai/workspace_python/Is_Setup/Config file')
        data = {
            'status' : 'OK',
            'data' : nationInfo
        }

    return data

def postToHub(POSId):
    query_args = { 'mode':'publish', 'topic':'http://140.109.22.197/static/Topic/'+POSId+"/"+POSId+'.json' }
    #query_args = { 'mode':'publish', 'topic':'http://140.109.22.197/static/Topic/985626/985626.json' }
    data = urllib.urlencode(query_args)
    url = 'http://project-hosting.iis.sinica.edu.tw/hub/php/'
    request = urllib2.Request(url,data)
    response = urllib2.urlopen(request)
    html = response.read()
    print html

def pushDB(data):
    data = (request.data).split('$')
    user = User.query.filter_by(id=login.current_user.get_id()).first()
    if data[0] == 'facility':
        shelter = Shelter(City=user.city, Id=data[1], Name=data[2].decode('utf8'),
                          Type=data[3].decode('utf8'),District=data[4].decode('utf8'),
                          Address=data[5].decode('utf8'),Telphone=data[6].decode('utf8'),
                          Latitude=data[7].decode('utf8'), Longitude=data[8].decode('utf8'),
                          Description=data[9].decode('utf8'),Category=data[10])

        db.session.add(shelter)
        db.session.commit()
    else :
        pos = POS(POS_city=user.city, POS_id=data[2], POS_district=data[3].decode('utf8'),
                  Partition_method='District',POS_latitude=data[4], POS_longitude=data[5],
                  Is_Available=False)

        db.session.add(pos)
        db.session.commit()

def insertUserInfo(configData):
    configData = configData.split('$')
    checkFolder(configData[0])

    user = User.query.filter_by(id=login.current_user.get_id()).first()
    user.country = configData[0]
    user.city = configData[1]
    db.session.commit()

def checkFolder(folderName):
    path = "C:/Users/Bai/workspace_python/Is_Setup/Config file/"+folderName
    if not os.path.exists(path):
        os.makedirs( path, 0755 )

def createFolder(folderName):
    path = "C:/Users/Bai/workspace_python/Is_Setup/static/Topic/"+folderName
    if not os.path.exists(path):
        os.makedirs( path, 0755 )


def fetchConfigInfo(country,city):
    filename = "C:/Users/Bai/workspace_python/Is_Setup/Config file/"+country+'/'+city+'.ini'
    if os.path.exists(filename):
        Info = []
        config = ConfigObj(filename)
        configInfo = {
                      "coordinates" : config['Country Information']['Origin Of Coordinates'],
                      "wardpath" : config['Country Information']['District Info Path'],
                      "key" : config['Boundary']['ApiKey'],
                      "posCountryCode" : config['POS Information']['POS_country_code']
        }
        return configInfo

def parseXmlFile(category):
    user = User.query.filter_by(id=login.current_user.get_id()).first()
    if category == 'district':
        regionInfo = []
        tree = ET.parse('C:/Users/Bai/workspace_python/Is_Setup/District Info/'+user.city+'.xml')
        root = tree.getroot()
        for info in root.findall('District'):
            data = {
                      "District" : info.find("Name").text,
                      "Code" : info.find("PostalCode").text
                   }
            regionInfo.append(data)
        return regionInfo
    else :
        tree = ET.parse('C:/Users/Bai/workspace_python/Is_Setup/UI Language file/Localization for UI.xml')
        root = tree.getroot()
        for menu in root.findall('Menu'):
            menuText = menu.find(user.ui_language).text
        for l in root.findall('Label'):
            labelText = l.find(user.ui_language).text
        for ptable in root.findall('POSTable'):
            ptableText = ptable.find(user.ui_language).text
        for stable in root.findall('SchemeTable'):
            stableText = stable.find(user.ui_language).text
        for tab in root.findall('Tab'):
            tabText = tab.find(user.ui_language).text
        for btn in root.findall('Button'):
            btnText = btn.find(user.ui_language).text
        for t in root.findall('Text'):
            words = t.find(user.ui_language).text
        UIInfo = {
                  "Menu" : menuText,
                  "Label" : labelText,
                  "POSTable" : ptableText,
                  "SchemeTable" : stableText,
                  "Tab" : tabText,
                  "Button" : btnText,
                  "Text" : words
               }
        return UIInfo

def search_dir_file(level, path):
    global allList
    dirList = []
    fileList = []
    diretory_info = []
    items = os.listdir(path)
    for f in items:
        if(os.path.isdir(path + '/' + f)):
            if(f[0] == '.'):
                pass
            else:
                dirList.append(f)
    for dl in dirList:
        allList={
                "Nation" : dl,
                "City":[]
        }
        files = os.listdir(path+ '/' + dl)
        for f in files:
            if(os.path.isfile(path + '/' + dl + '/' + f)):
                fileList.append(f)
                allList["City"].append({"Name":f[:-4]})
        diretory_info.append(allList)

    return diretory_info

def createNewConfig(configData):
    configData = configData.split('$')
    user = User.query.filter_by(id=login.current_user.get_id()).first()

    config = ConfigObj()
    config.filename = 'C:/Users/Bai/workspace_python/Is_Setup/Config file/'+user.country+'/'+user.city+'.ini'

    config['Country Information']={}
    config['Country Information']['Origin Of Coordinates']=configData[0]
    config['Country Information']['District Info Path']="C:/Users/Bai/workspace_python/Is_Setup/District Info/"+user.city+'.xml'

    config['Boundary']={}
    config['Boundary']['ApiKey']=configData[1]

    config['POS Information']={}
    config['POS Information']['POS_country_code']=""

    config.write()

def makeFile(content,type):
    user = User.query.filter_by(id=login.current_user.get_id()).first()
    filename = "C:/Users/Bai/workspace_python/Is_Setup/District Info/"+user.city+'.xml'
    f = open(filename, "w")
    f.write(content)
    f.close()

def downloadTxt(POSID,content):
    filename = 'C:/Users/Bai/workspace_python/Is_Setup/static/Topic/'+POSID+'/'+POSID+'.json'
    content = "".join(content.split())
    f = open(filename, "w")
    f.write(content)
    f.close()

def updatePOSDb(POSInfo):
    POSInfo = POSInfo.split('$')
    #user = User.query.filter_by(id=login.current_user.get_id()).first()
    for p in db.session.query(POS):
        if p.POS_id == POSInfo[0]:
            p.Partition_method = POSInfo[1]
            if p.Partition_method == 'District':
                p.Rectangle_coordinate1 = ''
                p.Rectangle_coordinate2 = ''
            else :
                p.Rectangle_coordinate1 = POSInfo[2]
                p.Rectangle_coordinate2 = POSInfo[3]
    db.session.commit()

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'

# Create in-memory database
app.config['DATABASE_FILE'] = 'sample_db.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# Create user model. For simplicity, it will store passwords in plain text.
# Obviously that's not right thing to do in real world application.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))
    country = db.Column(db.String(32))
    city = db.Column(db.String(32))
    ui_language = db.Column(db.String(100))
    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username

class POS(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    POS_id = db.Column(db.String(100))
    POS_city = db.Column(db.String(100))
    POS_district = db.Column(db.String(100))
    Partition_method = db.Column(db.Unicode(64))
    Rectangle_coordinate1 = db.Column(db.Unicode(64))
    Rectangle_coordinate2 = db.Column(db.Unicode(64))
    POS_latitude = db.Column(db.Unicode(64))
    POS_longitude = db.Column(db.Unicode(64))
    Is_Available = db.Column(db.Boolean, nullable=False)

    def __unicode__(self):
        return self.name


class Shelter(db.Model):
    Number = db.Column(db.Integer, primary_key=True)
    Id = db.Column(db.String(100))
    Name = db.Column(db.Unicode(64))
    City = db.Column(db.Unicode(100))
    Type = db.Column(db.Unicode(64))
    Category = db.Column(db.Unicode(64))
    District = db.Column(db.Unicode(100))
    Address = db.Column(db.Unicode(100))
    Telphone = db.Column(db.Unicode(64))
    Latitude = db.Column(db.Unicode(64))
    Longitude = db.Column(db.Unicode(64))
    Description = db.Column(db.Unicode(255))

    def __unicode__(self):
        return self.name

# Define login and registration forms (for flask-login)
class LoginForm(form.Form):
    login = fields.TextField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()


class RegistrationForm(form.Form):
    login = fields.TextField(validators=[validators.required()])
    email = fields.TextField()
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        if db.session.query(User).filter_by(login=self.login.data).count() > 0:
            raise validators.ValidationError('Duplicate username')

# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):

        userId = user_id
        return db.session.query(User).get(user_id)

# Create customized model view class
class MyModelView(sqla.ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated()
    def is_visible(self):
        if showMenuText == True:
            return True
        else :
            return False

# Create customized index view class that handles login & registration
class MyAdminIndexView(admin.AdminIndexView):
    @expose('/')
    def home(self):
        global showMenuText
        if not login.current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        for u in db.session.query(User):
            if login.current_user.get_id() == u.id:
                if u.country ==None:
                    showMenuText = False
                    return redirect(url_for('.initial_view'))
                else :
                    showMenuText = True
        return super(MyAdminIndexView, self).index()

    @expose('/initial/')
    def initial_view(self):
        return self.render('admin/setup1.html')

    @expose('/postUserInfo/', methods=['GET', 'POST'])
    def receiveUserInfo(self):
        if request.method == 'POST':
            insertUserInfo(request.data)
        return redirect(url_for('.countryView'))

    @expose('/country_config/')
    def countryView(self):
        return self.render('admin/setup2.html')

    @expose('/postCountryInfo/', methods=['GET', 'POST'])
    def receiveCountryInfo(self):
        if request.method == 'POST':
            createNewConfig(request.data)
            data = request.data.split('$')
            makeFile(data[2],'wardInfo')

    @expose('/ImportPOSInfo/')
    def POSView(self):
        return self.render('admin/setup3.html')

    @expose('/postPOSInfo/', methods=['GET', 'POST'])
    def receivePOSInfo(self):
        if request.method == 'POST':
            pushDB(request.data)
            data = request.data.split('$')
            user = User.query.filter_by(id=login.current_user.get_id()).first()
            filename = 'C:/Users/Bai/workspace_python/Is_Setup/Config file/'+user.country+'/'+user.city+'.ini'
            config = ConfigObj(filename)
            config['POS Information']['POS_country_code']=data[1]
            config.write()
            #menuText = parseXmlFile(user.ui_language)
            #showMenuText = True
            #text = menuText.split(',')
            #admin.add_view(ImportDataView(name=text[0]))
            #admin.add_view(MonitorView(name=text[1]))
            #admin.add_view(ContactView(name=text[2]))
        #return redirect(url_for('.monitorView'))

    @expose('/monitor/')
    def monitorView(self):
        return self.render('monitor.html')

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated():
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = User()

            form.populate_obj(user)

            db.session.add(user)
            db.session.commit()

            login.login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))

class ImportDataView(admin.BaseView):
    @admin.expose('/')
    def index(self):
        return self.render('InputFacData.html')
    def is_accessible(self):
        return login.current_user.is_authenticated()
    def is_visible(self):
        if showMenuText == True:
            return True
        else :
            return False

class ContactView(admin.BaseView):
    @admin.expose('/')
    def index(self):
        return self.render('contact.html')

    def is_accessible(self):
        return login.current_user.is_authenticated()


    def is_visible(self):
        if showMenuText == True:
            return True
        else :
            return False

class MonitorView(admin.BaseView):
    @admin.expose('/')
    def index(self):
        return self.render('monitor.html')


    def is_accessible(self):
        return login.current_user.is_authenticated()


    def is_visible(self):
        if showMenuText == True:
            return True
        else :
            return False

# Flask views
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/textView/')
def showText():
    return render_template('textview.html')

@app.route('/imgView/')
def showImg():
    return render_template('ImageView.html')


@app.route('/checkPOS/', methods=['POST', 'GET'])
def checkPOS_is_available():
    public_data = []
    for p in db.session.query(POS):
        mapdata={
            'id' : p.POS_id,
            'isContact' : p.Is_Available
        }
        public_data.append(mapdata)

    data = {
            'status' : 'OK',
            'data' : public_data
        }

    return jsonify(data)

@app.route('/whereAreURLs', methods=['POST', 'GET'])
def receiveLoc():
    count = 0
    latlng = request.args.get('latlng').split(',')
    for pos in db.session.query(POS):
        #print pos.POS_latitude
        if latlng[0] == pos.POS_latitude:
            count = count + 1
            POSID = pos.POS_id
            pos.Is_Available = True
            db.session.commit()


    if count == 0 :
        data = {
            'status' : 'OK',
            'hub_url' : 'http://project-hosting.iis.sinica.edu.tw/hub/php/',
            'topic_url' : 'wahahaha!!'
        }
    else :
        data = {
            'status' : 'OK',
            'hub_url' : 'http://project-hosting.iis.sinica.edu.tw/hub/php/',
            'topic_url' : 'http://140.109.22.197/static/Topic/'+POSID+'/'+POSID+".json"
        }

    return jsonify(data)


# Initialize flask-login
init_login()

# Create admin
admin = admin.Admin(app, 'MAD-IS', index_view=MyAdminIndexView(), base_template='my_master.html')
#admin = admin.Admin(index_view=MyAdminIndexView())
admin.add_view(MonitorView(name="Monitor"))

admin.add_view(ImportDataView(category='Data'))
admin.add_view(MyModelView(POS, db.session, category='Data'))
admin.add_view(MyModelView(Shelter, db.session, category='Data'))
admin.add_view(ContactView(name='Contact Us'))
def build_sample_db():
    """
    Populate a small db with some example entries.
    """

    import string
    import random

    db.drop_all()
    db.create_all()
    test_user = User(login="test", password="test")
    db.session.add(test_user)

    first_names = [
    ]

    for i in range(len(first_names)):
        user = User()
        user.first_name = first_names[i]
        user.last_name = last_names[i]
        user.login = user.first_name.lower()
        user.email = user.login + "@example.com"
        user.password = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10))
        db.session.add(user)

    names = [

    ]

    for i in range(len(names)):
        pos = POS()
        db.session.add(pos)

    sample_text = [
    ]

    for entry in sample_text:
        shelter = Shelter()
        db.session.add(shelter)

    db.session.commit()
    return


if __name__ == '__main__':
    # Build a sample db on the fly, if one does not exist yet.
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_sample_db()

    #app.run(debug=True)

    # Start app
    app.run(host= '140.109.22.197', port=int("80"))
