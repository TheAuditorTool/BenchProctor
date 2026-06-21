# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket


async def BenchmarkTest33211(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
