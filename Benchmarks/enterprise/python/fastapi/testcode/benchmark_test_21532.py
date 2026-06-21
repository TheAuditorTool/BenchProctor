# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest21532(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    yaml.safe_load(data)
    return {"updated": True}
