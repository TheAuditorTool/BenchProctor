# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import os
import tempfile


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest56119(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return {"updated": True}
