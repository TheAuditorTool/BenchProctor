# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import time


def to_text(value):
    return str(value).strip()

async def BenchmarkTest02522(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = to_text(upload_name)
    if time.time() > 1000000000:
        requests.get(str(data))
    return {"updated": True}
