# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import socket
from app_runtime import mq_client


async def BenchmarkTest48616(request: Request):
    msg_value = mq_client.get_message().body
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(msg_value)
    data = collected
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return {"updated": True}
