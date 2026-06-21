# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from urllib.parse import unquote


async def BenchmarkTest10671(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
