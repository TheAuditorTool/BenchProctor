# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


request_state: dict[str, str] = {}

async def BenchmarkTest44043(request: Request):
    auth_header = request.headers.get('authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    def _primary():
        subprocess.Popen('echo ' + str(data), shell=True).wait()
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
