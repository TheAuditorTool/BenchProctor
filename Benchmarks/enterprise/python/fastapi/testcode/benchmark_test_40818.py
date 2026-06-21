# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest40818(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = '{}'.format(xml_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
