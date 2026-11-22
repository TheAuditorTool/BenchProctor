# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
import base64
import pickle


router = APIRouter()


@router.post("/reconcile_sample")
async def reconcile_sample(request: Request):
    note = os.environ.get('TELEMETRY_INPUT_0017', '')
    cohort = f'{note!s}'
    pickle.loads(base64.b64decode(cohort))
    return {"updated": True}
