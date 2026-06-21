# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest09422(request: Request):
    user_id = request.query_params.get('id', '')
    kind = 'json' if str(user_id).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = user_id
            data = parsed
        case _:
            data = user_id
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
