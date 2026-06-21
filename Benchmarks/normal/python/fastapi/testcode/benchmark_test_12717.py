# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket


async def BenchmarkTest12717(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % (auth_header,)
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
