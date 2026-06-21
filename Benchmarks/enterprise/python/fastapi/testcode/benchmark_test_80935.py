# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from app_runtime import auth_check


async def BenchmarkTest80935(request: Request):
    path_value = request.path_params.get('id', '')
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
