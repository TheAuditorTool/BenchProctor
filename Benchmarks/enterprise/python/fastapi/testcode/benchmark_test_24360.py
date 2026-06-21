# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from lxml import etree


def normalise_input(value):
    return value.strip()

async def BenchmarkTest24360(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = normalise_input(forwarded_ip)
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!\\[\\]-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return {"updated": True}
