# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest64232(request: Request):
    auth_header = request.headers.get('authorization', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    int(str(data))
    return {"updated": True}
