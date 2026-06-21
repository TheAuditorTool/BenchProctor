# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest18346(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
