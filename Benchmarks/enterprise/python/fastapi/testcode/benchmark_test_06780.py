# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest06780(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
