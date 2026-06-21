# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
import json
from types import SimpleNamespace


async def BenchmarkTest30404(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
