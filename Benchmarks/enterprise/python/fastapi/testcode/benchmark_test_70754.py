# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


request_state: dict[str, str] = {}

async def BenchmarkTest70754(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    eval(compile("with open('/var/uploads/' + str(data), 'wb') as fh:\n    fh.write(b'data')", '<sink>', 'exec'))
    return {"updated": True}
