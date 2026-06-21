# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest43886(request: Request):
    secret_value = 'feature_flag_value'
    def normalize(value):
        return value.strip()
    data = normalize(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
