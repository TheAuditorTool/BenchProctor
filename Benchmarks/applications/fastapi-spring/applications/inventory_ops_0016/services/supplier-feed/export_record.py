# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/export_record")
async def export_record(request: Request):
    citation = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = str(citation).split(',')
    backorder = ' '.join(parts)
    with open('/var/app/data/' + str(backorder), 'w') as fh:
        fh.write('data')
    return {"updated": True}
