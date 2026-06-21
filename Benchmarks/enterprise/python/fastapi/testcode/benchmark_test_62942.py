# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest62942(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(dotenv_value))
    return {"updated": True}
