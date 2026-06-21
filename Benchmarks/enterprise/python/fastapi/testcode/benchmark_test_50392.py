# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import json
from app_runtime import db


async def BenchmarkTest50392(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
