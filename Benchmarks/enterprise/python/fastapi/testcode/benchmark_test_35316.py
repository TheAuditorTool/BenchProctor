# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


async def BenchmarkTest35316(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
