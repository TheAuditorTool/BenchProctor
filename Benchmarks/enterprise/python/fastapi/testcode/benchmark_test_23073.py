# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest23073(request: Request):
    referer_value = request.headers.get('referer', '')
    data = (lambda v: v.strip())(referer_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
