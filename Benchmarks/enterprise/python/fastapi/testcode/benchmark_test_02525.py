# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest02525(request: Request):
    path_value = request.path_params.get('id', '')
    data = default_blank(path_value)
    os.remove(str(data))
    return {"updated": True}
