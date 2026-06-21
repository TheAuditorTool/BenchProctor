# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import importlib


async def BenchmarkTest37972(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    importlib.import_module(str(data))
    return {"updated": True}
