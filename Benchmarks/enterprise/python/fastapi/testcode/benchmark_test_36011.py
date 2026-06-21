# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


request_state: dict[str, str] = {}

async def BenchmarkTest36011(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
