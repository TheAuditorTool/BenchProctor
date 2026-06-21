# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import ast
import urllib.request
import urllib.parse
import ssl


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest30334(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_OPTIONAL
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
