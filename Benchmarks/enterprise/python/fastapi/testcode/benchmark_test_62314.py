# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import tempfile


def relay_value(value):
    return value

async def BenchmarkTest62314(request: Request):
    user_id = request.query_params.get('id', '')
    data = relay_value(user_id)
    checked_path = os.path.normpath(data)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(checked_path))
    return {"updated": True}
