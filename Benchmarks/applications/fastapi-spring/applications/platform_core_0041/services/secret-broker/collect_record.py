# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/collect_record")
async def collect_record(request: Request):
    passage = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = str(passage).split(',')
    persona = ' '.join(parts)
    with open('/var/app/data/' + str(persona), 'w') as fh:
        fh.write('data')
    return {"updated": True}
