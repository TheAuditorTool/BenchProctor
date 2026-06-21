# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest53911(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    processed = 'true' if str(forwarded_ip).lower() in ('true', '1', 'yes', 'on') else 'false'
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return {"updated": True}
