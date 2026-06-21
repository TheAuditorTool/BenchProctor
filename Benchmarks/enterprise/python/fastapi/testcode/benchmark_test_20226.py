# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import re
from starlette.responses import JSONResponse


async def BenchmarkTest20226(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return {"updated": True}
