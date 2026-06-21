# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest03357(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '{}'.format(upload_name)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
