# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest09754(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = '%s' % (xml_value,)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
