# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest00184(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    pending = list(str(secret_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    db.connect(host='localhost', user='app', password=data)
    return {"updated": True}
