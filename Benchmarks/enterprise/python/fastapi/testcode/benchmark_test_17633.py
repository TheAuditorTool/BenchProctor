# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest17633(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = default_blank(upload_name)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
