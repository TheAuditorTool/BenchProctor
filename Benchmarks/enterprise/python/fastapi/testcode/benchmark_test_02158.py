# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest02158(request: Request):
    user_id = request.query_params.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    result = 100 / int(str(data))
    return {"updated": True}
