# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import json
from app_runtime import db


def ensure_str(value):
    return str(value)

async def BenchmarkTest41919(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
