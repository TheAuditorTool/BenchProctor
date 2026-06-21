# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest51498(request: Request):
    secret_value = 'app_display_name'
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(secret_value)
    data = collected
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
