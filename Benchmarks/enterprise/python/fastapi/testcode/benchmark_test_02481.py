# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest02481(request: Request):
    user_id = request.query_params.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    globals()['counter'] = int(data)
    return {"updated": True}
