# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest27276(request: Request):
    secret_value = 'feature_flag_value'
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(secret_value), store_cred)
    return {"updated": True}
