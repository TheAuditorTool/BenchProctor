# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest40201(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    reader = make_reader(header_value)
    data = reader()
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
