# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27001(request: Request):
    referer_value = request.headers.get('referer', '')
    data = referer_value if referer_value else 'default'
    eval(str(data))
    return {"updated": True}
