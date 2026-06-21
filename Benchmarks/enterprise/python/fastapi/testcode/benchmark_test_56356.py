# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest56356(request: Request):
    ua_value = request.headers.get('user-agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
