# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest78155(request: Request):
    host_value = request.headers.get('host', '')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(host_value), store_cred)
    return {"updated": True}
