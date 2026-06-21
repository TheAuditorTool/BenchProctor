# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest02029(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
