import cgi
import datetime
import urllib
import webapp2
import jinja2
import os

import httplib
import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


data=[{u'location': u'https://www.google.co.uk/maps/place/Hoxton+Square/@51.5273296,-0.0808067,17z/data=!3m1!4b1!4m2!3m1!1s0x48761cbadbc045ff:0x54292b8ccb0589c2', u'id': 1, u'address': u'Hoxton', u'name': u'Dr. Quinn Surgery'}, {u'location': u'https://www.google.co.uk/maps/place/Old+St/@51.5254642,-0.0879389,17z/data=!3m1!4b1!4m2!3m1!1s0x48761ca8abba80d9:0xd6cf02f1c545d61e', u'id': 2, u'address': u'Old Street', u'name': u'Doctor Dolittle'}]

  
class FrontPage(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.out.write(template.render())            
        
   

class LoginPage(webapp2.RequestHandler):

    def get(self):         
        template = JINJA_ENVIRONMENT.get_template('templates/login.html')
        self.response.out.write(template.render())

    def post(self):
        login_name=self.request.get('username')

        conn = httplib.HTTPConnection('192.168.3.64',8080)
        conn.request("GET", "/agilehackathon/rest/login/"+login_name)
        r1 = conn.getresponse()
        print r1.status, r1.reason
        
        if r1.status == 200:
            #self.response.out.write("<html>Hi %s! You've logged in successfully'</html>" % login_name)
            pracURL = "/agilehackathon/rest/practices/"+login_name
            
            conn.request("GET", pracURL)
            r2 = conn.getresponse()
            print "Logged in and getting list:", r2.status, r2.reason
            
            if r2.status == 200:
                #data = json.loads(r2.read())
                
                prac_list=[]
                for e in data:
                    prac_list.append(e['name'])
                
                template = JINJA_ENVIRONMENT.get_template('templates/practices.html')
                self.response.out.write(template.render(practices=data))#, name=login_name)
            #self.redirect('/list'+login_name)
        
        else:
            self.response.out.write("<html>Something went wrong! :-( <br> User not recognized...</html>")
        conn.close()
        

class ListPage(webapp2.RequestHandler):

    def get(self):         
        template = JINJA_ENVIRONMENT.get_template('templates/login.html')
        self.response.out.write(template.render())



app = webapp2.WSGIApplication([('/', FrontPage),
                               ('/list', ListPage),
                               ('/login', LoginPage)],
                              debug=True)
