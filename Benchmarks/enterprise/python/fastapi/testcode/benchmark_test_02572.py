# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest02572(request: Request):
    path_value = request.path_params.get('id', '')
    reader = make_reader(path_value)
    data = reader()
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
