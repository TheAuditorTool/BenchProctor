# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12197(request: Request):
    referer_value = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    request.session['user'] = str(data)
    return {"updated": True}
