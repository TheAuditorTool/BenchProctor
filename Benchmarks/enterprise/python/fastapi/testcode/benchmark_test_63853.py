# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote
from app_runtime import auth_check


async def BenchmarkTest63853(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
