# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest16866(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value}'
    result = 100 / int(str(data))
    return {"updated": True}
