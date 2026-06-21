# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest74670(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = auth_header if auth_header else 'default'
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
