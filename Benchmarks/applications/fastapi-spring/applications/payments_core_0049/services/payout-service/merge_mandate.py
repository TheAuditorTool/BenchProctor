# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
import base64
import pickle


router = APIRouter()


@router.post("/merge_mandate")
async def merge_mandate(request: Request):
    headline = os.environ.get('PAYMENTS_INPUT_0049', '')
    disbursement = f'{headline!s}'
    pickle.loads(base64.b64decode(disbursement))
    return {"updated": True}
