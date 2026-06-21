# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest66680(request: Request):
    host_value = request.headers.get('host', '')
    reader = make_reader(host_value)
    data = reader()
    yaml.safe_load(data)
    return {"updated": True}
