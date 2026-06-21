# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest81183(request: Request):
    user_id = request.query_params.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
