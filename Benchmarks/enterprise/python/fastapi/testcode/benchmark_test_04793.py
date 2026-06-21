# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04793(request: Request):
    referer_value = request.headers.get('referer', '')
    data = ' '.join(str(referer_value).split())
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
