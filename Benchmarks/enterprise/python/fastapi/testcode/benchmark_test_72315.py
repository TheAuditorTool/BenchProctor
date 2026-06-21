# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest72315(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
