# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import ast
from app_runtime import db


async def BenchmarkTest46824(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    try:
        data = str(ast.literal_eval(profile_value))
    except (ValueError, SyntaxError):
        data = profile_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
