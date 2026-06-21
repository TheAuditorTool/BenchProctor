# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote
from app_runtime import db


async def BenchmarkTest17492(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
