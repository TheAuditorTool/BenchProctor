# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
import subprocess


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest04710(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
