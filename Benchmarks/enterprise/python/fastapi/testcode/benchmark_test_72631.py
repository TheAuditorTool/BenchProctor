# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest72631(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
