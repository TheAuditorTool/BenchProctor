# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest19821(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data, _sep, _rest = str(secret_value).partition('\x00')
    db.connect(host='localhost', user='app', password=data)
    return {"updated": True}
