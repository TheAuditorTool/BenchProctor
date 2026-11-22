# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
import os
from starlette.responses import JSONResponse
from pathlib import Path
from app_runtime import db


router = APIRouter()


@router.post("/compact_config")
async def compact_config(request: Request):
    headline = db.fetch_one('SELECT name FROM users LIMIT 1')
    disbursement = json.loads(headline).get('value', '')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, disbursement))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    remittance = full_path
    Path(remittance).write_text('data')
    return {"updated": True}
