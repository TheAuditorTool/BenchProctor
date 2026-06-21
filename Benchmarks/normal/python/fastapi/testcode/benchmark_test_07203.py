# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07203(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    exec(str(data))
    return {"updated": True}
