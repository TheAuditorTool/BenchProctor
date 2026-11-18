# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/reconcile_profile")
async def reconcile_profile(request: Request):
    phrase = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        parcel = json.loads(phrase).get('value', phrase)
    except (json.JSONDecodeError, AttributeError):
        parcel = phrase
    allowed = {'config.json', 'index.html', 'readme.md'}
    if parcel not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    consignment = '/var/app/data/' + parcel
    with open(consignment, 'w') as fh:
        fh.write('data')
    return {"updated": True}
