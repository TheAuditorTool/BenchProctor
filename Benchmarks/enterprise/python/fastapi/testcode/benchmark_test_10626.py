# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
import time
from types import SimpleNamespace
import subprocess


async def BenchmarkTest10626(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
