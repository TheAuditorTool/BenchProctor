# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
import json


async def BenchmarkTest40152(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
