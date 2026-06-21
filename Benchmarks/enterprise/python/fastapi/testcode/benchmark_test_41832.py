# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest41832(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
