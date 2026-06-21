# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import os
import importlib
import sys


@dataclass
class FormData:
    payload: str

async def BenchmarkTest75905(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
