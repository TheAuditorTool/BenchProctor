# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest71135(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
