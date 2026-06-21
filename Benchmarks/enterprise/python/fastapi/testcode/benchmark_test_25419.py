# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def ensure_str(value):
    return str(value)

async def BenchmarkTest25419(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = ensure_str(xml_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
