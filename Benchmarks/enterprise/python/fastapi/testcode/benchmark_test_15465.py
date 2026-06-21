# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest15465(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '%s' % (multipart_value,)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
