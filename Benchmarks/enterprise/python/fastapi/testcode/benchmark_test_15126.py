# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest15126(request: Request):
    path_value = request.path_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
