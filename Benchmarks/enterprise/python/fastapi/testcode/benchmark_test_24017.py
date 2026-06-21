# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest24017(request: Request):
    user_id = request.query_params.get('id', '')
    data = default_blank(user_id)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
