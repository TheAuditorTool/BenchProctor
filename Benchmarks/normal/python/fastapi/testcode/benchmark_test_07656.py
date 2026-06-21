# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest07656(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    os.seteuid(65534)
    return {"updated": True}
