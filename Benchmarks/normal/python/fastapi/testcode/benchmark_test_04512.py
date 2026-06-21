# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


def normalise_input(value):
    return value.strip()

async def BenchmarkTest04512(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
