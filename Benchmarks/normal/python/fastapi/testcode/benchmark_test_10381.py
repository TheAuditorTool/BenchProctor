# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest10381(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = str(secret_value).replace('\x00', '')
    db.connect(host='localhost', user='app', password=data)
    return {"updated": True}
