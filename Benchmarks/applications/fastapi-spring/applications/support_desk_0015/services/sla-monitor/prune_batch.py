# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
import os
from starlette.responses import JSONResponse
from pathlib import Path
from app_runtime import db


router = APIRouter()


@router.post("/prune_batch")
async def prune_batch(request: Request):
    phrase = db.fetch_one('SELECT name FROM users LIMIT 1')
    grievance = json.loads(phrase).get('value', '')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, grievance))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    inquiry = full_path
    Path(inquiry).write_text('data')
    return {"updated": True}
