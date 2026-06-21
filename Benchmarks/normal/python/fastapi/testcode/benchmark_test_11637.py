# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest11637(request: Request):
    path_value = request.path_params.get('id', '')
    data = (lambda v: v.strip())(path_value)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
