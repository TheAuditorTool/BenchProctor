# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote
from app_runtime import auth_check


async def BenchmarkTest43728(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
