# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest28929(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = f'{secret_value:.200s}'
    db.connect(host='localhost', user='app', password=data)
    return {"updated": True}
