# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import os


request_state: dict[str, str] = {}

async def BenchmarkTest71791(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    def _primary():
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
