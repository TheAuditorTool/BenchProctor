# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest65662(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    importlib.import_module(str(data))
    return {"updated": True}
