# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


request_state: dict[str, str] = {}

async def BenchmarkTest20055(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    processed = data[:64]
    yaml.load(processed, Loader=yaml.UnsafeLoader)
    return {"updated": True}
