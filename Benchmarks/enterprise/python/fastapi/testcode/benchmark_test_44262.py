# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import importlib
import sys


async def BenchmarkTest44262(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
