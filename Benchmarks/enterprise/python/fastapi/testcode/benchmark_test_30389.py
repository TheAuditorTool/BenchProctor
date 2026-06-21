# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest30389(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    kind = 'json' if str(xml_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = xml_value
            data = parsed
        case _:
            data = xml_value
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
