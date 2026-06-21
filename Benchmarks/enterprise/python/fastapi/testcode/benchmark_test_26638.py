# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def relay_value(value):
    return value

async def BenchmarkTest26638(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = relay_value(xml_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
