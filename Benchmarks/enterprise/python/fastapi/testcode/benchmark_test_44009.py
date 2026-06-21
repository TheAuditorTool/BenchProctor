# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest44009(request: Request):
    path_value = request.path_params.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'w') as fh:
            fh.write('data')
    await _evasion_task()
    return {"updated": True}
