# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest20969(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
