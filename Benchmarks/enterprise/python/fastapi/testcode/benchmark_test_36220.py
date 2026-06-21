# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest36220(request: Request):
    path_value = request.path_params.get('id', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(path_value) + ',data\n')
    return {"updated": True}
