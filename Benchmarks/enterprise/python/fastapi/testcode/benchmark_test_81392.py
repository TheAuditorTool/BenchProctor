# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest81392(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = xml_value.decode('utf-8', 'ignore') if isinstance(xml_value, bytes) else xml_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
