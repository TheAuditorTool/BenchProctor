# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
import subprocess


async def BenchmarkTest76432(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
