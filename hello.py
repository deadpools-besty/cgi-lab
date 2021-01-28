#!/usr/bin/env python3
import os
import json
import templates
import sys
import secret
# print('Content-Type: application/json')
# print()
# print(json.dumps(dict(os.environ), indent=2))

# cookies set up stolen from: https://www.tutorialspoint.com/How-to-setup-cookies-in-Python-CGI-Programming

print(f"Set-Cookie:username = {secret.username}")
print(f"Set-Cookie:password = {secret.password}")
print('Content-Type: text/html')
print()
print(templates.login_page())


posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes: 
    posted = sys.stdin.read(int(posted_bytes))
    print(f"<p> POSTED: <pre>")
    for line in posted.splitlines():
        print(line)
    print("</pre></p>")


# print('''
# <!doctyoe html>
# <htmml>
# <body>
# <h1>Hello world</h1>
# <ul>
# ''')
# print(f"<p> Browser={os.environ['HTTP_USER_AGENT']}")
# print('''d
# </ul>
# </body>
# </html>
# ''')