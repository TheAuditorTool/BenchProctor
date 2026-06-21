# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03187(request: Request):
    host_value = request.headers.get('host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    request.session['data'] = str(data)
    return {"updated": True}
