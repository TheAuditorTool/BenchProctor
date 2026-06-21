# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02681(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
