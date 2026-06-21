# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest64038(request: Request):
    path_value = request.path_params.get('id', '')
    kind = 'json' if str(path_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = path_value
            data = parsed
        case _:
            data = path_value
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
