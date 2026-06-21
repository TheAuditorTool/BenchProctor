# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import tempfile


def relay_value(value):
    return value

async def BenchmarkTest59206(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return {"updated": True}
