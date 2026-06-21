# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest77357(request: Request):
    path_value = request.path_params.get('id', '')
    kind = 'json' if str(path_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = path_value
            data = parsed
        case _:
            data = path_value
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
