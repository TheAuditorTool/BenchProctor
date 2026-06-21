# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest48672(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = xml_value if xml_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
