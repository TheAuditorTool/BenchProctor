# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import requests


async def BenchmarkTest58770(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
