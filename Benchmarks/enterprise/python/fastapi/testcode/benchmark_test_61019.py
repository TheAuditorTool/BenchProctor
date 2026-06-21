# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest61019(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(header_value),))
    return {"updated": True}
