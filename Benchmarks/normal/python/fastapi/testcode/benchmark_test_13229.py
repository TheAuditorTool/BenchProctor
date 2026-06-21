# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest13229(request: Request):
    path_value = request.path_params.get('id', '')
    prefix = ''
    data = prefix + str(path_value)
    json.loads(data)
    return {"updated": True}
