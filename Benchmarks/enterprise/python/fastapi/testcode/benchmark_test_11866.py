# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import json


async def BenchmarkTest11866(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    logging.info('User action: ' + str(data))
    return {"updated": True}
