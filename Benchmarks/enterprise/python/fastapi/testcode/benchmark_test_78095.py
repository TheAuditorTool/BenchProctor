# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest78095(request: Request, field: str = Form('')):
    field_value = field
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(field_value).replace('\r', '').replace('\n', ''))
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
