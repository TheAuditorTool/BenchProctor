# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest12597(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = '%s' % str(xml_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
