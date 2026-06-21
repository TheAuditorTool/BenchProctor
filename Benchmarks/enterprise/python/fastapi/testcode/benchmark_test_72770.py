# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import importlib
import sys


def to_text(value):
    return str(value).strip()

async def BenchmarkTest72770(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = to_text(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return {"updated": True}
