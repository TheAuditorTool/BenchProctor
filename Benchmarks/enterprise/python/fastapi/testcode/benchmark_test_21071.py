# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest21071(request: Request):
    path_value = request.path_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
