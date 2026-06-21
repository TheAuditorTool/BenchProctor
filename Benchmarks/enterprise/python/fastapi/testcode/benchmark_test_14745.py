# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest14745(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(prop_value)
    data = collected
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
