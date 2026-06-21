# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import importlib
import sys


async def BenchmarkTest11497(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
