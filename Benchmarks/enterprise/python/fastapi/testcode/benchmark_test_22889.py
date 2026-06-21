# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import re
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest22889(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = default_blank(cookie_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return {"updated": True}
