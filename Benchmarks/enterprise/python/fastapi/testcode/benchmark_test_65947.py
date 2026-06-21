# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest65947(request: Request):
    referer_value = request.headers.get('referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
