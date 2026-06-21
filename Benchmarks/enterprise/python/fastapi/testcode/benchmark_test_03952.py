# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest03952(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = ' '.join(str(secret_value).split())
    db.connect(host='localhost', user='app', password=data)
    return {"updated": True}
