# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import re
from starlette.responses import JSONResponse


async def BenchmarkTest28951(request: Request):
    origin_value = request.headers.get('origin', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(origin_value)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = origin_value
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return {"updated": True}
