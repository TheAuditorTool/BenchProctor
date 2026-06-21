# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest12885(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % (path_value,)
    os.remove(str(data))
    return {"updated": True}
