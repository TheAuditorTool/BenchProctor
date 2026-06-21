# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

async def BenchmarkTest10850(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = FormData(payload=prop_value).payload
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
