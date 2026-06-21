# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest71168(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
