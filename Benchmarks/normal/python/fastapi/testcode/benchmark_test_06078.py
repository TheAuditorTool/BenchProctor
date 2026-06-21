# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import tempfile


def normalise_input(value):
    return value.strip()

async def BenchmarkTest06078(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return {"updated": True}
