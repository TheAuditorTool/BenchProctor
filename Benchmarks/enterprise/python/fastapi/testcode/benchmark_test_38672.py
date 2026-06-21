# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest38672(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = ' '.join(str(upload_name).split())
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
