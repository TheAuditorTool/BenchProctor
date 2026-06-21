# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest61950(request: Request):
    path_value = request.path_params.get('id', '')
    kind = 'json' if str(path_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = path_value
            data = parsed
        case _:
            data = path_value
    request.session['user'] = str(data)
    return {"updated": True}
