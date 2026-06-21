# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import ast
from app_runtime import db


async def BenchmarkTest44547(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    def _primary():
        requests.get(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
