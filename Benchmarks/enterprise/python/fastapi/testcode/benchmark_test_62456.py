# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest62456(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
