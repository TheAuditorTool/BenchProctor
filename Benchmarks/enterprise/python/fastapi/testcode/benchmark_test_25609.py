# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest25609(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
