# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import json
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest00495(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
