# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest53898(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    kind = 'json' if str(xml_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = xml_value
            data = parsed
        case _:
            data = xml_value
    os.system('echo ' + str(data))
    return {"updated": True}
