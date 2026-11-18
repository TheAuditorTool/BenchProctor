# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/validate_device")
async def validate_device(request: Request):
    phrase = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = str(phrase).split(',')
    persona = ' '.join(parts)
    with open('/var/app/data/' + str(persona), 'w') as fh:
        fh.write('data')
    return {"updated": True}
