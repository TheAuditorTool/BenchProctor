# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


async def BenchmarkTest20075(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
