# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest78998(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name}'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
