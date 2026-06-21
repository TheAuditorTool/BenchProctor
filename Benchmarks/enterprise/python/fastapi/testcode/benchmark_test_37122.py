# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import socket


request_state: dict[str, str] = {}

async def BenchmarkTest37122(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        s = socket.create_connection((str(data), 80))
        s.close()
    return {"updated": True}
