# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest25508(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    kind = 'json' if str(raw_body).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = raw_body
            data = parsed
        case _:
            data = raw_body
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
