from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('',8001,application)
print("server httpd on port 8001.....")


httpd.serve_forever()


