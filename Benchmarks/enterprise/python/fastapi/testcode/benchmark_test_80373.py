# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

async def BenchmarkTest80373(request: Request):
    secret_value = 'default_config_label'
    data = ensure_str(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
