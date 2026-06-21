# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest66573(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
