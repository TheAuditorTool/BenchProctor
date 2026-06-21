# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from app_runtime import auth_check


async def BenchmarkTest32089(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
