# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39743(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    kind = 'json' if str(forwarded_ip).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = forwarded_ip
            data = parsed
        case _:
            data = forwarded_ip
    eval(str(data))
    return {"updated": True}
