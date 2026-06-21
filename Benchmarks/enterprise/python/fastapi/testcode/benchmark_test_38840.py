# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote
from app_runtime import auth_check


async def BenchmarkTest38840(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
