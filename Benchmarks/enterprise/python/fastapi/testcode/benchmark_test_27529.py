# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest27529(request: Request):
    path_value = request.path_params.get('id', '')
    request_state['last_input'] = path_value
    data = request_state['last_input']
    eval(compile("_resp = requests.get(str(data))\ndb.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))", '<sink>', 'exec'))
    return {"updated": True}
