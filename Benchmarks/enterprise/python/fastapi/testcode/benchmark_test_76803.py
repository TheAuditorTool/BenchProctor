# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from dataclasses import dataclass
from fastapi import Form
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest76803(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
