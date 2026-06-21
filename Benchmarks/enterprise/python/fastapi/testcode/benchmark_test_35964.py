# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from app_runtime import auth_check


async def BenchmarkTest35964(request: Request):
    secret_value = 'app_display_name'
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
