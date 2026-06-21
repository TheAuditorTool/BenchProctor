# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest10645(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
