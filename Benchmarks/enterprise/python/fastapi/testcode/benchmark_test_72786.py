# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest72786(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
