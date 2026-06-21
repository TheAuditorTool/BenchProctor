# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest47844(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '{}'.format(raw_body)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
