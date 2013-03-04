#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
from google.appengine.ext.webapp import template

class PageHandler(webapp2.RequestHandler):
 def get(self):
   base_url = self.request.path
   if self.request.path == '/':
     self.redirect("http://webrtc.googlecode.com/svn/trunk/" 
                    + "samples/js/demos/index.html"
                    , permanent=True)
   else:
     self.redirect("http://webrtc.googlecode.com/svn/trunk/" 
                    + "samples/js/demos"
                    + base_url, 
                    permanent=True)

app = webapp2.WSGIApplication([
  (r'/*.*', PageHandler),
 ], debug=True)
