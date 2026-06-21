# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest63856(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = (lambda v: v.strip())(file_value)
    auth_check('user', data)
    return {"updated": True}
