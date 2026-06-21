# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


def to_text(value):
    return str(value).strip()

async def BenchmarkTest00416(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = to_text(header_value)
    def _primary():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
