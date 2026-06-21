# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest24002(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    eval(compile("_resp = requests.get(str(data))\ndb.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))", '<sink>', 'exec'))
    return {"updated": True}
