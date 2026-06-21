# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from types import SimpleNamespace


async def BenchmarkTest65262(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
