# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest54493(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
