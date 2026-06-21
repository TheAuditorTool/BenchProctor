# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
from pydantic import BaseModel
from starlette.responses import JSONResponse
import asyncio


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest01954(request: Request, req: UserInput):
    json_value = req.payload
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = await fetch_payload()
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return {"updated": True}
