# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import importlib


async def BenchmarkTest75996(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    importlib.import_module(str(data))
    return {"updated": True}
