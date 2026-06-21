# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest59063(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = default_blank(ua_value)
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
