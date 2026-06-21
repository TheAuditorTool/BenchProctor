# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from types import SimpleNamespace


async def BenchmarkTest80037(request: Request):
    origin_value = request.headers.get('origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
