# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import time


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest56363(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = default_blank(upload_name)
    if time.time() > 1000000000:
        requests.get(str(data))
    return {"updated": True}
