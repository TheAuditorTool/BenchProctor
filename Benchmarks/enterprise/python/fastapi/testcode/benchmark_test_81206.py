# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


def to_text(value):
    return str(value).strip()

async def BenchmarkTest81206(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
