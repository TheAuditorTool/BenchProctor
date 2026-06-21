# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest06412(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    os.system('echo ' + str(data))
    return {"updated": True}
