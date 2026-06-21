# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest22141(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
