# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from types import SimpleNamespace


async def BenchmarkTest54289(request: Request):
    path_value = request.path_params.get('id', '')
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
