# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest76719(request: Request):
    path_value = request.path_params.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    eval(compile("subprocess.run('echo ' + str(data), shell=True)", '<sink>', 'exec'))
    return {"updated": True}
