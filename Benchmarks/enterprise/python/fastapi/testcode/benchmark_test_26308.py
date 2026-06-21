# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest26308(request: Request):
    path_value = request.path_params.get('id', '')
    reader = make_reader(path_value)
    data = reader()
    yaml.safe_load(data)
    return {"updated": True}
