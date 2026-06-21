# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest66868(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '{}'.format(ua_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
