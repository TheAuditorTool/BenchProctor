# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest61232(request: Request):
    secret_value = 'config_secret_test_abc123'
    data = to_text(secret_value)
    db.connect(host='localhost', user='app', password=data)
    return {"updated": True}
