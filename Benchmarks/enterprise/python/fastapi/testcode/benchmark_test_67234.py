# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


def relay_value(value):
    return value

async def BenchmarkTest67234(request: Request):
    secret_value = 'default_setting_value'
    data = relay_value(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
