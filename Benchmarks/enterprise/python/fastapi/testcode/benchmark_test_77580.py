# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest77580(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(prop_value), store_cred)
    return {"updated": True}
