# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


async def BenchmarkTest11896(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
