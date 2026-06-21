# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


request_state: dict[str, str] = {}

async def BenchmarkTest77736(request: Request):
    upload_name = request.query_params.get('filename', '')
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    def _primary():
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
