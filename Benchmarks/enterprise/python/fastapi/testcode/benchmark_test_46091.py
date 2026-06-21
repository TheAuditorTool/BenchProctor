# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest46091(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = ' '.join(str(secret_value).split())
    db.connect(host='localhost', user='app', password=data)
    return {"updated": True}
