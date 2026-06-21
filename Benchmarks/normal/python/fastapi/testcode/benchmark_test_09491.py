# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest09491(request: Request):
    user_id = request.query_params.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
