# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import ast
import urllib.request
import urllib.parse
import ssl
from app_runtime import db


async def BenchmarkTest47975(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = str(ast.literal_eval(db_value))
    except (ValueError, SyntaxError):
        data = db_value
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
