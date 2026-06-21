# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest63512(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    os.remove(str(data))
    return {"updated": True}
