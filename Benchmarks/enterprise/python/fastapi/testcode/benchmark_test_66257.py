# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest66257(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value}'
    int(str(data))
    return {"updated": True}
