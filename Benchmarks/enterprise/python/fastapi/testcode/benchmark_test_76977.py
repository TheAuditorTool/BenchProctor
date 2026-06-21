# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from types import SimpleNamespace
import subprocess


async def BenchmarkTest76977(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    def _primary():
        subprocess.run([str(data), '--status'], shell=False)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
