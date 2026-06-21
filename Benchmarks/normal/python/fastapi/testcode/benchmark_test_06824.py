# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest06824(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(header_value), store_cred)
    return {"updated": True}
