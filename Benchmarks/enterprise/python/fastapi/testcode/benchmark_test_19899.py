# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import json


async def BenchmarkTest19899(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    logging.info('User action: ' + str(data))
    return {"updated": True}
