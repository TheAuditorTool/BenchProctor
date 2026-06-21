# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest43045(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
