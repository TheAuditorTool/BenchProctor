# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest02947(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    auth_check('user', file_value)
    return {"updated": True}
