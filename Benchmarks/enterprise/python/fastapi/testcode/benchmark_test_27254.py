# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

async def BenchmarkTest27254(request: Request):
    path_value = request.path_params.get('id', '')
    data = to_text(path_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
