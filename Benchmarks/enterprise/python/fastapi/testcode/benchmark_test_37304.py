# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import socket


def to_text(value):
    return str(value).strip()

async def BenchmarkTest37304(request: Request):
    user_id = request.query_params.get('id', '')
    data = to_text(user_id)
    if not re.match(r'^.{1,256}$', str(data)):
        return JSONResponse({'error': 'schema invalid'}, status_code=400)
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
