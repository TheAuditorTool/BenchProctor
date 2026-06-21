# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import ast
from app_runtime import db


async def BenchmarkTest38665(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = str(ast.literal_eval(db_value))
    except (ValueError, SyntaxError):
        data = db_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
