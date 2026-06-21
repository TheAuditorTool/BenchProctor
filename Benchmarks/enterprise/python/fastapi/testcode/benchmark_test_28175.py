# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from types import SimpleNamespace


async def BenchmarkTest28175(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        yaml.load(data, Loader=yaml.UnsafeLoader)
    await _evasion_task()
    return {"updated": True}
