# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest70375(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
