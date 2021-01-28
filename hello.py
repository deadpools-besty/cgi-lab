#!/usr/bin/env python3
import os
import json
import templates
# print('Content-Type: application/json')
# print()
# print(json.dumps(dict(os.environ), indent=2))

print('Content-Type: text/html')
print()
templates.login_page()
# print('''
# <!doctyoe html>
# <htmml>
# <body>
# <h1>Hello world</h1>
# <ul>
# ''')
# print(f"<p> Browser={os.environ['HTTP_USER_AGENT']}")
# print('''
# </ul>
# </body>
# </html>
# ''')