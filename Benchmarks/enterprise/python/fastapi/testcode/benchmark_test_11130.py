# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest11130(request: Request):
    user_id = request.query_params.get('id', '')
    kind = 'json' if str(user_id).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = user_id
            data = parsed
        case _:
            data = user_id
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
