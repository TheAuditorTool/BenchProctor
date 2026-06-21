# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39427(request: Request):
    path_value = request.path_params.get('id', '')
    data = (lambda v: v.strip())(path_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
