# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest55482(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
