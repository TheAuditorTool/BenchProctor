# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest42889(request: Request):
    host_value = request.headers.get('host', '')
    kind = 'json' if str(host_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = host_value
            data = parsed
        case _:
            data = host_value
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
