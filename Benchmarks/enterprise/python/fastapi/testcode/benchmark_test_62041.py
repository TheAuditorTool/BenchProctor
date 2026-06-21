# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest62041(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
