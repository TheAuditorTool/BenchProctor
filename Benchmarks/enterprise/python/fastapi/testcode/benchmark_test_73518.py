# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

async def BenchmarkTest73518(request: Request):
    secret_value = 'default_setting_value'
    data = normalise_input(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
