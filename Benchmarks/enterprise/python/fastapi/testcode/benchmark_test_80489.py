# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import importlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest80489(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    importlib.import_module(str(data))
    return {"updated": True}
