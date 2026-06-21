# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest37528(request: Request):
    ua_value = request.headers.get('user-agent', '')
    kind = 'json' if str(ua_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = ua_value
            data = parsed
        case _:
            data = ua_value
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
