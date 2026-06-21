# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest07691(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
