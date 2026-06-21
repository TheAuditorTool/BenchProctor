# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest27587(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
