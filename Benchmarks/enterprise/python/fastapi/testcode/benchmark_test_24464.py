# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest24464(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value}'
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
