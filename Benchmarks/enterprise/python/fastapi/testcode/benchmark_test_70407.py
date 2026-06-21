# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest70407(request: Request):
    origin_value = request.headers.get('origin', '')
    kind = 'json' if str(origin_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = origin_value
            data = parsed
        case _:
            data = origin_value
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
