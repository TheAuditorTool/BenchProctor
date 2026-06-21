# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import json
from app_runtime import db


async def BenchmarkTest01150(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(graphql_var),))
    logging.info('audit actor=%s action=revoke_sessions', str(graphql_var))
    return {"updated": True}
