# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest73290(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '{}'.format(multipart_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
