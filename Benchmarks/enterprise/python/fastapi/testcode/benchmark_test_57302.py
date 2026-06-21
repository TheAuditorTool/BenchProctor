# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest57302(request: Request):
    referer_value = request.headers.get('referer', '')
    data = referer_value if referer_value else 'default'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
