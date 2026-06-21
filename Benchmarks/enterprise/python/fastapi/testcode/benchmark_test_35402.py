# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest35402(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    yaml.safe_load(data)
    return {"updated": True}
