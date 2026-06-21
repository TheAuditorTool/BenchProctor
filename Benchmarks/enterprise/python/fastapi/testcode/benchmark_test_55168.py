# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest55168(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value}'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
