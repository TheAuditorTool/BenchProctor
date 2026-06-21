# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest10374(request: Request):
    secret_value = 'config_secret_test_abc123'
    data = normalise_input(secret_value)
    db.connect(host='localhost', user='app', password=data)
    return {"updated": True}
