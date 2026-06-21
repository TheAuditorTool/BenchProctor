# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import importlib
import sys


async def BenchmarkTest22232(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
