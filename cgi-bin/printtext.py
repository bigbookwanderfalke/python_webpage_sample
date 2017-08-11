#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import sys
import io

html_body = """
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>Hello Python - print get text</title>
    </head>
    <body>
        <h1>%s</h1>
    </body>
</html>
"""
form = cgi.FieldStorage()
s = form.getvalue('testtext', '')
print(html_body % s)

