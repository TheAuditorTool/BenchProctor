# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest55388(request: Request):
    path_value = request.path_params.get('id', '')
    if path_value:
        data = path_value
    else:
        data = ''
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
