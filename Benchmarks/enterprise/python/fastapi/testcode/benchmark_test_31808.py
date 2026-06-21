# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest31808(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = ' '.join(str(dotenv_value).split())
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
