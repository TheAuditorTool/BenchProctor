# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import tempfile


async def BenchmarkTest25968(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(env_value))
    os.chmod(path, 0o777)
    return {"updated": True}
