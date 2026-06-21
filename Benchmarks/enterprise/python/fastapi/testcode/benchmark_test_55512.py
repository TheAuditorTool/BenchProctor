# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest55512(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
