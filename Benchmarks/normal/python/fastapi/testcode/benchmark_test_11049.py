# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


async def BenchmarkTest11049(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    async def _evasion_task():
        yaml.load(data, Loader=yaml.UnsafeLoader)
    await _evasion_task()
    return {"updated": True}
