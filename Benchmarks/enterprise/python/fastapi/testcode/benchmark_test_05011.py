# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05011(request: Request):
    user_id = request.query_params.get('id', '')
    kind = 'json' if str(user_id).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = user_id
            data = parsed
        case _:
            data = user_id
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
