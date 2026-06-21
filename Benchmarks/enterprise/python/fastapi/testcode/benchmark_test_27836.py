# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27836(request: Request):
    referer_value = request.headers.get('referer', '')
    data = referer_value if referer_value else 'default'
    exec(str(data))
    return {"updated": True}
