# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest18088(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    kind = 'json' if str(xml_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = xml_value
            data = parsed
        case _:
            data = xml_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
