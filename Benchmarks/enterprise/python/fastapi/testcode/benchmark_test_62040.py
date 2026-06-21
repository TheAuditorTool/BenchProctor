# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import re
from fastapi import Form
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest62040(request: Request, field: str = Form('')):
    field_value = field
    data = normalise_input(field_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return {"updated": True}
