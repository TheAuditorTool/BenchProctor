# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest10168(request: Request):
    upload_name = (await request.form()).get('upload', '')
    kind = 'json' if str(upload_name).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = upload_name
            data = parsed
        case _:
            data = upload_name
    os.system('echo ' + str(data))
    return {"updated": True}
