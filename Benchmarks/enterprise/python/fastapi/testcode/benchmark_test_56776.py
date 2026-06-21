# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest56776(request: Request):
    path_value = request.path_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    os.seteuid(65534)
    return {"updated": True}
