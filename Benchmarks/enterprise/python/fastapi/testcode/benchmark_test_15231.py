# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest15231(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = (lambda v: v.strip())(secret_value)
    db.connect(host='localhost', user='app', password=data)
    return {"updated": True}
