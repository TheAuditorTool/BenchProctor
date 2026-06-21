# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest21895(request: Request):
    auth_header = request.headers.get('authorization', '')
    kind = 'json' if str(auth_header).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = auth_header
            data = parsed
        case _:
            data = auth_header
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
