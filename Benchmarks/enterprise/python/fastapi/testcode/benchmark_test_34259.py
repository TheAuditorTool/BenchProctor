# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import ast
import urllib.request
import urllib.parse
import ssl
from app_runtime import db


async def BenchmarkTest34259(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
