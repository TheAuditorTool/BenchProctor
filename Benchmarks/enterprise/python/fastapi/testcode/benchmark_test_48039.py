# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

async def BenchmarkTest48039(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = ensure_str(forwarded_ip)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
