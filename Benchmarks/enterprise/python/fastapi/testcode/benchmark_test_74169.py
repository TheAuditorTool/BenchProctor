# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import importlib
import sys


async def BenchmarkTest74169(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
