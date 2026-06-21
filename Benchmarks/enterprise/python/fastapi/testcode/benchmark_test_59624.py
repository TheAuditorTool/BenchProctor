# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import importlib


async def BenchmarkTest59624(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    importlib.import_module(str(data))
    return {"updated": True}
