# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
from dataclasses import dataclass
import json
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest12223(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
