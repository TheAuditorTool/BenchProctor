# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


request_state: dict[str, str] = {}

async def BenchmarkTest18614(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
