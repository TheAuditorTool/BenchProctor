# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest73648(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
