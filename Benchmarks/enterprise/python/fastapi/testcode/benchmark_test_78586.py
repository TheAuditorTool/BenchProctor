# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import auth_check


async def BenchmarkTest78586(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = json.loads(file_value).get('value', '')
    auth_check('user', data)
    return {"updated": True}
