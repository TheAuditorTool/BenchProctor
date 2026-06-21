# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest35334(request: Request):
    secret_value = 'default_config_label'
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(secret_value), store_cred)
    return {"updated": True}
