# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket


async def BenchmarkTest50127(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % (user_id,)
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
