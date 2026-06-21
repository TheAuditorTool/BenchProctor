# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest42502(request: Request):
    path_value = request.path_params.get('id', '')
    reader = make_reader(path_value)
    data = reader()
    json.loads(data)
    return {"updated": True}
