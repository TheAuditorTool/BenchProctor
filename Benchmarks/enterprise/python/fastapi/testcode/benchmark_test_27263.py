# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
import urllib.request
from app_runtime import db


async def BenchmarkTest27263(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
