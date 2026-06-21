# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest17584(request: Request):
    secret_value = 'default_setting_value'
    if secret_value:
        data = secret_value
    else:
        data = ''
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
