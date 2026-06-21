# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27924(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
