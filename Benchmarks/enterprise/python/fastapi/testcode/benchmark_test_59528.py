# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest59528(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % (auth_header,)
    auth_check('user', data)
    return {"updated": True}
