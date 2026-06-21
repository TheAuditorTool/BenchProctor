# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import socket
from app_runtime import mq_client


def ensure_str(value):
    return str(value)

async def BenchmarkTest63819(request: Request):
    msg_value = mq_client.get_message().body
    data = ensure_str(msg_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JSONResponse({'error': 'schema invalid'}, status_code=400)
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
