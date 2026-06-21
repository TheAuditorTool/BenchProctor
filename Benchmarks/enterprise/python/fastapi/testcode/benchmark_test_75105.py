# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest75105(request: Request):
    path_value = request.path_params.get('id', '')
    os.chmod('/var/app/data/' + str(path_value), 0o777)
    return {"updated": True}
