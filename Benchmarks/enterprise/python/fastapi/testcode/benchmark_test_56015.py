# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest56015(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
