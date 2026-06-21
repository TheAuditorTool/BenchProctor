# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37012(request: Request):
    referer_value = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    eval(str(data))
    return {"updated": True}
