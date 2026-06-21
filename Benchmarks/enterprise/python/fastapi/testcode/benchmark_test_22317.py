# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest22317(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    requests.get('https://api.pycdn.io/data', params={'q': str(xml_value)}, verify=False)
    return {"updated": True}
