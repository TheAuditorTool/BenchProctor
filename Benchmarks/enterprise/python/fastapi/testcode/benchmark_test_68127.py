# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest68127(request: Request):
    path_value = request.path_params.get('id', '')
    with open(os.path.join('/var/app/data', str(path_value)), 'r') as fh:
        content = fh.read()
    return content
