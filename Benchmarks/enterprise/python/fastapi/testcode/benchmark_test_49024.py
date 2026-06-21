# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import importlib


def relay_value(value):
    return value

async def BenchmarkTest49024(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = relay_value(upload_name)
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return {"updated": True}
