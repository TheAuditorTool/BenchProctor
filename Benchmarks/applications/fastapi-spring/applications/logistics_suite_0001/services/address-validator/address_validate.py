# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/validate_address")
async def validate_address(request: Request):
    quotation = (await request.json()).get('payload', '')
    reader = make_reader(quotation)
    parcel = reader()
    requests.post("http://carrier-gateway:8080/DispatchCarrier", json={"shipping_payload": str(parcel)})
    return {"updated": True}
