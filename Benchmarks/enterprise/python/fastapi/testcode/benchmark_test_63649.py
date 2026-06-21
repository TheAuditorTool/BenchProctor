# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest63649(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
