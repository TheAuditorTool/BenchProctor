# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03036(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
