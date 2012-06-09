#!/usr/bin/python
# Web server to Arduino gateway
# POST data is sent to the Arduino over the serial link
#
# Copyright 2009 Ken Shirriff
# http://arcfn.com
import cgi
import serial
import eiscp

from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
receiver = eiscp.eISCP('10.0.1.41', 60128)
receiver.connectSocket()
# The web server.
class MyHandler(SimpleHTTPRequestHandler):
  def do_POST(self):
    if self.path == '/control':
      global receiver
      form = cgi.FieldStorage(fp=self.rfile, headers=self.headers,
        environ={'REQUEST_METHOD':'POST'})
      code = form['code'].value
      print 'Sent:', code
      receiver.writeCommandFromName(code)
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      return
    return self.do_GET()

# You may need something other than /dev/ttyUSB0
server = HTTPServer(('', 8080), MyHandler).serve_forever()
