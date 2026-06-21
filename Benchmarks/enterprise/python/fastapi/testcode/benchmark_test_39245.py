# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


async def BenchmarkTest39245(request: Request):
    secret_value = 'config_secret_test_abc123'
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    db.connect(host='localhost', user='app', password=data)
    return {"updated": True}
