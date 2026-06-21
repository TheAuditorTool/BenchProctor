# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import shlex
import json


async def BenchmarkTest35640(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
