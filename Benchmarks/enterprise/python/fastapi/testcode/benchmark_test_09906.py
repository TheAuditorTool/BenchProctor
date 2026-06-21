# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest09906(request: Request):
    origin_value = request.headers.get('origin', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    request.session['data'] = str(data)
    return {"updated": True}
