# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest07691(request: Request):
    secret_value = 'app_display_name'
    data = default_blank(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
