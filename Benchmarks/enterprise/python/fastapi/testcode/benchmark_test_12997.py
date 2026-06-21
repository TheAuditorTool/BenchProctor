# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


request_state: dict[str, str] = {}

async def BenchmarkTest12997(request: Request):
    auth_header = request.headers.get('authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    def _primary():
        subprocess.run('echo ' + str(data), shell=True)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
