# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest32332(request: Request):
    upload_name = (await request.form()).get('upload', '')
    kind = 'json' if str(upload_name).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = upload_name
            data = parsed
        case _:
            data = upload_name
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
