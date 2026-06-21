# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def normalise_input(value):
    return value.strip()

async def BenchmarkTest60210(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = normalise_input(upload_name)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
