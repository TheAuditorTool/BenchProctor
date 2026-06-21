# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import importlib


async def BenchmarkTest43100(request: Request):
    host_value = request.headers.get('host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    importlib.import_module(str(data))
    return {"updated": True}
