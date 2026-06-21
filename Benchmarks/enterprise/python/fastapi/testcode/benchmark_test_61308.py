# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


def normalise_input(value):
    return value.strip()

async def BenchmarkTest61308(request: Request):
    path_value = request.path_params.get('id', '')
    data = normalise_input(path_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
