# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


def to_text(value):
    return str(value).strip()

async def BenchmarkTest47456(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = to_text(header_value)
    eval(compile('importlib.import_module(str(data))', '<sink>', 'exec'))
    return {"updated": True}
