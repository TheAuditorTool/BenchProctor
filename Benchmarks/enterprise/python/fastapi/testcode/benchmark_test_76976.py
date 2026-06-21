# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest76976(request: Request):
    user_id = request.query_params.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return {"updated": True}
