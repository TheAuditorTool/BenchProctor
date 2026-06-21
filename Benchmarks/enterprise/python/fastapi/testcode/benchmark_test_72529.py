# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest72529(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
