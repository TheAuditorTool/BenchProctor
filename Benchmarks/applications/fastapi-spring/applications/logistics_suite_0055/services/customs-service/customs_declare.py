# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/declare_customs")
async def declare_customs(request: Request):
    heading = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    consignment = normalize(heading)
    requests.post("http://rate-shopper:8080/ShopRate", json={"shipping_payload": str(consignment)})
    return {"updated": True}
