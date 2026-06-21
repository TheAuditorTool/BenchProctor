# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest74860(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % str(path_value)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
