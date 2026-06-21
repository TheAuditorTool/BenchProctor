# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest10099(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return {"updated": True}
