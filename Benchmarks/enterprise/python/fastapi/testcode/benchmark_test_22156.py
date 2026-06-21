# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import json


async def BenchmarkTest22156(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    logging.info('User action: ' + str(data))
    return {"updated": True}
