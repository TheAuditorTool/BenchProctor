# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest57644(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
